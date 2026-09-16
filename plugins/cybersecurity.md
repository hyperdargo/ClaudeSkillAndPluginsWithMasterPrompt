# cybersecurity

OSS-only security work: OWASP Top 10, penetration testing, vulnerability testing (XSS, SSRF, CSRF, business-logic flaws, Host header attacks), threat modeling with STRIDE and MITRE ATT&CK, Sigma detection rules, SAST and code audit, and AI/LLM red-teaming.

- **Marketplace:** `claude-skills`
- **Source:** https://github.com/secondsky/claude-skills
- **Version in this bundle:** 3.9.0
- **License:** MIT

## Install

```
/plugin marketplace add https://github.com/secondsky/claude-skills.git
/plugin install cybersecurity@claude-skills
```

The marketplace only needs adding once — after that, install the rest with a
single `/plugin install <name>@claude-skills` each.

## When it fires

Runs the security phase of the master prompt. Use it when you need real coverage instead of a vibes-based 'looks secure to me'. It deliberately favours open-source tooling over paid suites (Burp, Nessus, Splunk).

## Notes

Only run active testing against systems you are authorised to test.
