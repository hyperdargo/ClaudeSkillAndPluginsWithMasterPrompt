"""Copy selected skills while preserving every existing target folder."""
import argparse
from pathlib import Path
import shutil

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--skill", action="append", default=[])
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1] / "skills"
    available = {p.name: p for p in source.iterdir() if (p / "SKILL.md").is_file()}
    unknown = set(args.skill) - set(available)
    if unknown:
        parser.error("Unknown skill(s): " + ", ".join(sorted(unknown)))
    target = args.target.expanduser().resolve()
    repo = source.parent
    if target == repo or repo in target.parents:
        parser.error("Choose an installation directory outside this collection repository.")
    copied = skipped = 0
    for name in sorted(set(args.skill) or available):
        destination = target / name
        if destination.exists() or destination.is_symlink():
            print("SKIP existing: " + name)
            skipped += 1
            continue
        if args.dry_run:
            print("WOULD COPY: " + name)
        else:
            target.mkdir(parents=True, exist_ok=True)
            shutil.copytree(available[name], destination)
            print("COPIED: " + name)
        copied += 1
    print(f"{'Planned' if args.dry_run else 'Copied'}: {copied}; preserved existing: {skipped}")

if __name__ == "__main__":
    main()
