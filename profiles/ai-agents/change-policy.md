# AI Agent Change Policy

## Before editing
- Verify repository, branch, HEAD, working tree and untracked files.
- Read applicable root/nested agent instructions and relevant architecture/tests/CI.
- Identify user-owned changes, generated files and sensitive material.
- Define scope, acceptance checks and risk for material tasks.

## During editing
- Keep diffs focused and reversible.
- Follow existing conventions and approved contracts.
- Protect secrets; do not weaken checks merely to pass CI.
- Update tests, documentation, schemas and migrations when behavior changes.

## Verification
- Run targeted tests, then relevant broader checks.
- Inspect command exit status, final diff and repository state.
- Report skipped/blocked checks honestly.
- For failures, report them and avoid unsupported success claims.

## Completion report
State objective, changed files, decisions, commit/PR status, checks and results, limitations, risks and next steps.
