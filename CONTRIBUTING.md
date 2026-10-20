# Contributing to NUEGS

Explain the governance problem, affected profiles/domains and evidence. Keep changes small. Identify normative policy versus informative guidance. Use stable unique IDs. Update schemas, tests, examples, mappings and changelog as needed. Record compatibility and migration impact. Do not claim external-standard conformity without scoped evidence.

## Local checks
```bash
python -m unittest discover -s tests -v
python tooling/validate_registry.py
python tooling/resolve_profile.py niceone-obsidian
python tooling/resolve_profile.py ai-agents
```

## Pull request checklist
- [ ] Scope, owner and rationale are clear.
- [ ] Applicable controls and domains are identified.
- [ ] IDs remain unique and stable.
- [ ] Tests ran and results are reported accurately.
- [ ] Risks, exceptions and evidence implications are documented.
- [ ] Version/changelog updated where required.
