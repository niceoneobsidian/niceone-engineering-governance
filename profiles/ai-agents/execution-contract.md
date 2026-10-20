# AI Agent Execution Contract

1. Discover repository, branch, HEAD, working tree, instructions, architecture, tests and CI before editing.
2. Resolve authority and report conflicts rather than silently choosing a source.
3. Define objective, allowed paths, prohibited actions and acceptance criteria.
4. Plan changed files, risk, tests, dependencies and rollback.
5. Preserve user changes; do not overwrite unrelated work.
6. Make minimal, coherent edits; do not add dependencies without reason.
7. Run relevant checks and inspect final diff/state.
8. On failure, inspect current state before retrying; avoid destructive cleanup.
9. Report changed paths, commit/PR status, checks actually run, results, limitations and risks.

Distinguish observed facts, inferences and proposals. A code change is not tested because tests exist. A PR is not merged because it was opened. Do not claim a clean tree, successful push, deployment or compliance without evidence.

Stop before unauthorized destructive changes, production operations, external publication, material cost, sensitive-data exposure or permission changes. High-risk actions need explicit action-specific authorization enforced by a trusted boundary.
