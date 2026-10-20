# OIS and Agent Weave Adoption Pilot — Initial Remote Assessment

**Assessment date:** 2026-10-20  
**Purpose:** Start the two-profile adoption pilot without overstating implementation or compliance.  
**Method:** Read-only inspection of GitHub repository metadata, selected instructions, README files, and recent workflow runs. No local checkout, working-tree state, secrets, deployment environment, or live execution boundary was inspected.

## Target revisions

| Target | Canonical repository | Branch | Inspected revision | Assessment limit |
|---|---|---|---|---|
| Niceone Obsidian (OIS) | [niceoneobsidian/niceone-obsidian](https://github.com/niceoneobsidian/niceone-obsidian) | `main` | `7b94c0bc749681241ce2e7fa22aceb929c089591` | Remote metadata and selected docs/workflows only |
| Niceone Agent Weave | [niceoneobsidian/niceone-agent-weave](https://github.com/niceoneobsidian/niceone-agent-weave) | `master` | `a04d79641cfa883c180a64b185dba4380d12ed82` | Private repo metadata and selected docs/config/tests listing only |

These are the revisions visible during this assessment. Re-run the pilot if either target branch moves before sign-off.

## A. OIS profile — initial control map

| NUEGS concern | Observed evidence | Preliminary state | Required next verification |
|---|---|---|---|
| Agent instructions and architecture | `AGENTS.md` instructs context verification, atomic modifications, tests and zero-guess behavior. It references `../niceone-cli/workspace/standards/ENGINEERING_STANDARDS.md`. | **PARTIAL** | Verify the referenced path exists in the actual agent workspace; an external relative path is not portable by itself. Inspect `CLAUDE.md`, other instruction files and precedence rules. |
| Development and tests | `CONTRIBUTING.md` specifies Python 3.12+, Ruff, Mypy and a bounded offline pytest command; integration/live/sandbox tests require separate approval. | **DOCUMENTED** | Run the prescribed offline checks in a controlled checkout and capture exact results. Keep infrastructure-dependent suites separate. |
| CI/security evidence | Recent [Gitleaks run 39397814011](https://github.com/niceoneobsidian/niceone-obsidian/actions/runs/39397814011) failed; [OSV-Scanner run 39227574844](https://github.com/niceoneobsidian/niceone-obsidian/actions/runs/39227574844) and [OpenSSF Scorecard run 39225698483](https://github.com/niceoneobsidian/niceone-obsidian/actions/runs/39225698483) succeeded on the inspected revision. | **MIXED / OPEN** | Triage Gitleaks findings with secret-safe handling. A scanner failure is not proof of an exposed credential, and a pass is not proof of total security. |
| Branch protection | Not verified by this remote inspection. | **NOT ASSESSED** | Read effective branch rules using owner access and test direct-push/failing-check rejection. |
| Authorization and execution | Documentation emphasizes governance, but no runtime execution tests were run in this pilot. | **NOT ASSESSED** | Trace protected actions to actual runtime/CI/deployment enforcement, test denial and approval paths, retain logs. |
| State, recovery and audit evidence | Not assessed from source/test execution in this pass. | **NOT ASSESSED** | Map relevant modules and tests, execute failure/recovery scenarios, retain evidence tied to the revision. |
| Adoption decision | Not ready for a compliance claim. | **BLOCKED** | OIS owner reviews the control map, test evidence, unresolved risks and exceptions. |

### OIS evidence boundary
The Gitleaks result must be triaged before the security control can be accepted. Do not copy potentially sensitive findings into public reports. Record finding identifiers, disposition, and safe evidence references only.

## B. Agent Weave profile — initial control map

| NUEGS concern | Observed evidence | Preliminary state | Required next verification |
|---|---|---|---|
| Agent scope and instructions | `.clinerules` says edit only task-named files, preserve assertions unless requested, avoid git commands, and run pytest. | **DOCUMENTED / NEEDS RECONCILIATION** | Reconcile these instructions with README guidance and actual supported commands; test which instruction sources each agent consumes. |
| Independent verification | README states a task is complete only when an independent verify command exits 0 and reports at least one test; without a verify command, the task is blocked. | **DOCUMENTED** | Execute success, failure, zero-tests, and missing-verifier cases; confirm the recorded task state and evidence. |
| Permission policy | README describes deny-by-default command checks, human approval for push-like operations, withholding secret-looking environment variables, protected-path checks and bounded retries. | **DOCUMENTED, NOT VERIFIED HERE** | Inspect `config/permissions.json`, `docs/security.md` and execution code; run negative tests for destructive commands, protected paths, missing approval, secret handling and retry exhaustion. |
| Tests and CI | Repository lists unittest test files; README documents `PYTHONPATH=src python3 -m unittest discover -s tests -v`. The `.clinerules` instead mandates `python -m pytest tests/ -q`. No GitHub Actions runs were returned for this repository query. | **PARTIAL** | Run the README test command from the actual repository checkout; resolve the pytest/unittest mismatch and add a CI workflow or document why CI is intentionally absent. |
| Release/branch governance | Not verified. | **NOT ASSESSED** | Inspect repository rules, branch configuration and change approval behavior. |
| Adoption decision | No executed test outputs were collected by this assessment. | **BLOCKED** | Agent Weave owner reviews findings, runs tests and supplies evidence for every control marked tested or verified. |

## Pilot-wide evidence rules

For every applicable NUEGS control, the full pilot record must include:
- Stable control ID and selected profile.
- Target repository, branch and exact commit.
- Implementation location or explicit `not_found`.
- Test/review method and command.
- Result, timestamp and actor/reviewer.
- Evidence URI or artifact identifier.
- Limitations, risk, owner and remediation issue.

Use only these assessment states:
- `not_assessed`: evidence has not been collected.
- `documented`: written intent exists, runtime behavior unverified.
- `implemented`: implementation location identified.
- `tested`: an appropriate test ran and its result is recorded.
- `verified`: evidence satisfies the control's acceptance criteria.
- `adopted`: the target owner accepts the mapping, evidence, exceptions and ongoing review obligations.
- `blocked`: a release-blocking condition remains.

Never promote a control from documentation to verified without execution or independent inspection evidence.

## Exit criteria
- [ ] Current target revisions reconfirmed at sign-off.
- [ ] OIS offline test tier executed and results recorded.
- [ ] OIS Gitleaks findings triaged without disclosing secret material.
- [ ] OIS branch protection and protected-operation enforcement tested.
- [ ] Agent Weave unittest suite executed and pytest/unittest instruction conflict resolved.
- [ ] Agent Weave permission, destructive-action, approval, recovery and independent-verification tests executed.
- [ ] Control maps reviewed and signed off by each target owner.
- [ ] Open findings have owners, priorities, remediation targets and explicit risk acceptance where applicable.

**Disposition: initial remote assessment only. Neither target is declared NUEGS-compliant or fully adopted.**
