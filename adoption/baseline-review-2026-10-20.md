# NUEGS Baseline Review and Adoption Assessment

**Assessment date:** 2026-10-20  
**Assessed revision:** `584b25df3ae224bab149a428b7c1b3111b68b48a` (main)  
**Scope:** NUEGS repository baseline, registries, reference tooling, tests, CI and GitHub enforcement metadata.  
**Assessment type:** Remote repository review. No local checkout, external runtime, or downstream production environment was inspected.  
**Disposition:** Initial specification is usable as a draft; adoption gates remain open.

## Executive result

The repository's validation workflow passed on the assessed main revision. This proves that the configured unit tests and registry/profile commands passed for that revision. It does **not** prove that the governance controls are enforced or that OIS/AI-agent target repositories comply.

The most material finding is repository-level enforcement: GitHub's branch API reported `protected: false`, and the rulesets endpoint returned an empty list. The initial PR was merged without a submitted PR review. A separate request to read the branch-protection endpoint returned 403, so its detailed settings could not be inspected; the branch metadata and empty ruleset list are the available evidence.

## Evidence ledger

| ID | Observation | Evidence | Assessment |
|---|---|---|---|
| AUD-001 | Main branch metadata reports `protected: false`. | GitHub branch API for `main`, assessed 2026-10-20. | **P0 — open.** Required checks/reviews are not evidenced as enforced. |
| AUD-002 | Ruleset API returned an empty list. | GitHub repository rulesets endpoint, assessed 2026-10-20. | **P0 — open.** No repository ruleset is visible to this integration. |
| AUD-003 | PR #1 was merged; the PR review list was empty. | PR #1 metadata and reviews endpoint. | **P1 — open.** A passing CI run is not a substitute for independent review. |
| AUD-004 | NUEGS validation workflow completed successfully on main. | [Run 39357521919](https://github.com/niceoneobsidian/niceone-engineering-governance/actions/runs/39357521919), commit `584b25d`. | **Passed within scope.** Tests do not currently validate every registry relationship or JSON Schema constraint. |
| AUD-005 | Registry validator checks required files, IDs, some risk/evidence fields, domain files and profile gate shape. | `tooling/validate_registry.py`. | **P1 — partial.** Enforcement-map references/statuses and metric/standard fields are not comprehensively cross-checked. |
| AUD-006 | Policy evaluator is explicitly labelled a reference tool, but arbitrary action names can reach an allow result and the boolean authorization/approval inputs do not bind to a specific action/resource/expiry. | `tooling/evaluate_policy.py`. | **P1 — fix reference semantics; never use as runtime enforcement.** |
| AUD-007 | Evidence schema is JSON Schema, but tests only parse schema files and check the `$schema` marker; no JSON Schema validator is used. | `tests/test_schemas.py`, `schemas/*.schema.json`. | **P1 — scope mismatch.** Tests verify syntax, not conformance to the declared schema. |
| AUD-008 | Repository license is an all-rights-reserved notice, not an OSI-approved open-source license. | `LICENSE`, repository metadata. | **Decision required.** Public visibility does not grant reuse rights. |
| AUD-009 | Standard registry deliberately marks some references as candidates or says to verify current editions. | `standards/standards-registry.yaml`. | **Acceptable with follow-up.** Do not claim standards conformity until scoped mappings and evidence exist. |
| AUD-010 | Enforcement map marks controls `not_verified`. | `controls/enforcement-map.yaml`. | **Correct status.** Do not promote these to verified without implementation evidence. |

## Control adoption status

- **Specification artifacts:** present on main.
- **Local deterministic validation:** passed in the recorded GitHub Actions run.
- **GitHub repository protection:** not evidenced; current API metadata indicates unprotected main.
- **Independent policy review:** not evidenced for the initial PR.
- **OIS implementation and runtime authorization:** not assessed in this repository-only pass.
- **AI-agent runtime permission enforcement:** not assessed in this repository-only pass.
- **External standard conformity:** not assessed.
- **Open-source licensing:** not decided.

## Required corrective actions

### P0 — enforce the repository boundary
1. Configure a ruleset or branch protection for `main`.
2. Require pull requests and at least one approving review where the account/plan supports it; prevent self-approval from satisfying the requirement.
3. Require the stable check name **NUEGS registry and policy tests** before merge.
4. Block force pushes and branch deletion; apply rules to administrators/bypass actors unless a documented emergency process says otherwise.
5. Capture a settings screenshot/export and run a negative test showing a direct push or failing-check merge is rejected. Do not call the control verified until the negative test is evidenced.

### P1 — make validation claims accurate
1. Cross-check control IDs referenced by the enforcement map.
2. Validate metric profile values, unique IDs, required fields and standard registry status fields.
3. Add tests for malformed and cross-referenced registry data.
4. Narrow the reference policy evaluator to known actions and require both authorization and approval for protected actions; retain the warning that it is not an enforcement boundary.
5. Either implement actual JSON Schema validation as a declared dependency or rename/document the current tests as schema-syntax checks.

### P1 — formal decisions
1. Decide whether this public repository is intended to be open source. If yes, select an appropriate license explicitly; if no, retain the restrictive notice and describe the intended distribution.
2. Assign a maintainer/control owner and review cadence.
3. Create a downstream pilot audit for OIS and AI Agents. Use evidence from the exact target revision; do not infer local worktree state from GitHub branch state.

## Exit criteria for adoption

NUEGS may be described as **adopted for this repository** only after:
- main protection and required checks are configured and negatively tested;
- the registry validator and policy reference semantics are corrected and CI passes;
- a maintainer has reviewed and accepted the normative baseline;
- licensing intent is recorded;
- controls have owners and review dates.

Even then, this means the specification repository is governed. It does not mean downstream repositories or deployed systems are compliant.
