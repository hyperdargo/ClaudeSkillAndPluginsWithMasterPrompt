"""Validate package inventory and normalized skill content hashes."""
import hashlib
import json
from pathlib import Path

def main():
    root = Path(__file__).resolve().parents[1]
    catalog = json.loads((root / "catalog.json").read_text(encoding="utf-8"))
    ids, paths, errors = set(), set(), []
    for item in catalog["skills"]:
        if item["id"] in ids:
            errors.append("Duplicate ID: " + item["id"])
        ids.add(item["id"])
        relative = item["path"] + "/SKILL.md"
        if relative in paths:
            errors.append("Duplicate path: " + relative)
        paths.add(relative)
        path = (root / relative).resolve()
        if root not in path.parents or not path.is_file():
            errors.append("Missing or invalid path: " + relative)
            continue
        digest = hashlib.sha256(path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()
        if digest != item["sha256"]:
            errors.append("Hash mismatch: " + relative)
    actual = {p.as_posix() for folder in ["skills", "platform-skills"] for p in (root / folder).glob("**/SKILL.md") if p.is_file()}
    expected = {str((root / p).as_posix()) for p in paths}
    # Nested example SKILL.md files are supporting material, not top-level packages.
    top_level = {p.as_posix() for pattern in ["skills/*/SKILL.md", "platform-skills/*/*/SKILL.md"] for p in root.glob(pattern)}
    if top_level != expected:
        errors.append("Top-level inventory differs from catalog")
    if not expected.issubset(actual):
        errors.append("Catalog references missing skill files")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Verified {len(ids)} unique packages and normalized content hashes.")

if __name__ == "__main__":
    main()
