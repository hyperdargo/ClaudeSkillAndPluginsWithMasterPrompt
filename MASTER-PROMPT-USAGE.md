# Use the master prompt

[MASTER-PROMPT.md](MASTER-PROMPT.md) contains the v3.0 website and software engineering standard.

## Direct use

Write a concrete project brief, then paste the master prompt below it. Include your goal, audience, content, preferred stack, constraints, existing repository and what completion means.

```text
Project: A hotel website using the existing repository.
Audience: Guests comparing rooms and planning a stay.
Primary action: Send a booking enquiry.
Content: Use only supplied room details, photographs and contact information.
Constraints: Preserve working routes; support mobile and reduced motion.
Done when: The build passes and the main enquiry flow has been checked.

[Paste MASTER-PROMPT.md here.]
```

## Install the router skill

```sh
python scripts/install_skills.py --target ~/.claude/skills --skill master-website-engineering
```

Ask the assistant to use `master-website-engineering`. Its `reference/master-prompt.md` contains the same standard as the root prompt. Host tools still need to be available independently.

## Working with the standard

Supply real business content, identify missing details, and state which actions are authorized. Ask for an honest report of changes and checks performed. A prompt does not provide browser tools, security scanners, deployment credentials or plugin services on its own.
