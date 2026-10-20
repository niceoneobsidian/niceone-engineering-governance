# Niceone Unified Engineering Governance Specification (NUEGS)

NUEGS is the versioned, evidence-based engineering governance specification for Niceone repositories. It defines reusable rules and profiles for Niceone Obsidian (OIS) and AI coding agents.

> NUEGS defines the rules. Profiles define how rules apply. Repositories implement controls. Recorded evidence determines what has actually been verified.

## Status
- Current version: see [VERSION](VERSION) (0.1.0).
- Release status: **v1.0 not released; readiness gates remain open**.
- Latest readiness assessment: [NUEGS v1.0 readiness gate](adoption/v1.0-readiness-2026-10-20.md).
- Adoption assessment: [OIS and Agent Weave pilot](adoption/ois-agent-weave-pilot-2026-10-20.md).
- Release requirements: [RELEASE.md](RELEASE.md).
- Profiles: [Niceone Obsidian](profiles/niceone-obsidian/profile.yaml), [AI Agents](profiles/ai-agents/profile.yaml).
- Domain coverage: 20 domains listed in [domain registry](domains/domain-registry.yaml).

## Structure
- `foundations/`: authority, principles, risk, exceptions, lifecycle.
- `standards/`: external standard references and mapping rules.
- `profiles/`: profile-specific controls and acceptance gates.
- `domains/`: 20 engineering-domain profiles.
- `controls/`: canonical control registry and enforcement map.
- `metrics/`: metric definitions.
- `schemas/`: machine-readable schema contracts.
- `tooling/`: registry validation, profile resolution, policy evaluation.
- `tests/`: deterministic tests.
- `adoption/`: audits, rollout and maturity guidance.

## Run locally
Requires Python 3.12+. Registry files use JSON syntax, which is valid YAML, so registry tooling needs only the standard library. The test suite uses the pinned JSON Schema dependency in `requirements-dev.txt` to validate registry entries against schemas.

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
python tooling/validate_registry.py
python tooling/resolve_profile.py niceone-obsidian
python tooling/resolve_profile.py ai-agents
python tooling/evaluate_policy.py --profile ai-agents --action read --risk R0
```

The policy evaluator is a reference tool, not an authorization service. Real permissions must be enforced by trusted runtime, GitHub, CI, operating-system or deployment controls.

## Rules
1. Applicable law, contracts and mandatory security obligations take precedence.
2. Prompts and model outputs do not grant permissions.
3. Controls require owners, stable IDs, verification methods and evidence.
4. Missing or failed required checks are not passes.
5. Exceptions must be scoped, approved, risk-assessed and time-limited.
6. Do not claim compliance, certification or production readiness from documentation alone.
7. Preserve OIS capability maturity separately: `UNKNOWN → DESIGNED → IMPLEMENTED → TESTED → INTEGRATED → DEPLOYED → ACTIVATED → PRODUCTION VERIFIED`.

NUEGS control lifecycle: `Proposed → Defined → Implemented → Tested → Verified → Adopted`. See [GOVERNANCE.md](GOVERNANCE.md) and [rollout plan](adoption/rollout-plan.md).

## Review and adoption
- [Baseline review (2026-10-20)](adoption/baseline-review-2026-10-20.md): original findings and exit criteria.
- [v1.0 readiness gate (2026-10-20)](adoption/v1.0-readiness-2026-10-20.md): explicit status for all eight completion outcomes and release blockers.
- [OIS and Agent Weave pilot (2026-10-20)](adoption/ois-agent-weave-pilot-2026-10-20.md): initial remote-only target assessment.
- [Release policy](RELEASE.md): versioning, release evidence and mandatory v1.0 gates.
- [P0 main-branch protection issue](https://github.com/niceoneobsidian/niceone-engineering-governance/issues/3).
- [P1 licensing decision](https://github.com/niceoneobsidian/niceone-engineering-governance/issues/4).
- [P1 OIS and AI-agent pilot](https://github.com/niceoneobsidian/niceone-engineering-governance/issues/5).

Do not mark a target compliant or adopted until its current revision, implementation, tests, enforcement and evidence have been independently reviewed.
