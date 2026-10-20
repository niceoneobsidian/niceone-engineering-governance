# NUEGS Release Policy

## Release authority

A release tag identifies an exact, reviewed commit. It does not certify every repository that references NUEGS. The release record must state the scope assessed, tests executed, known gaps, approved exceptions and evidence limitations.

## Versioning

- Use semantic versioning for the specification contract.
- MAJOR: incompatible normative requirements, control semantics, schemas or profile behavior.
- MINOR: backward-compatible normative additions or new capabilities.
- PATCH: compatible clarifications and non-normative corrections.
- Keep the repository `VERSION`, changelog heading, tag and GitHub release version aligned.
- Do not reuse stable control/domain IDs. Document migration paths for breaking changes.

## Required v1.0 gates

The v1.0 readiness report is authoritative for the current evidence and status. Before release:
1. The specification and both profiles receive independent review.
2. CI validates schemas, registries, cross-references and profile resolution on the exact release commit.
3. Policy positive and negative cases pass; the reference evaluator is not described as trusted authorization.
4. Main-branch protection and bypass rejection are verified through actual platform behavior.
5. OIS and Agent Weave pilots record exact revisions, test results, evidence, exceptions and open risks.
6. Every verified/adopted claim is supported by inspectable evidence.
7. The repository owner explicitly confirms licensing intent.
8. All P0 blockers are closed or the release is deferred. Do not waive legal duties or represent unresolved enforcement as complete.
9. An independent reviewer approves the release commit.
10. The tag and release notes identify the exact approved commit and scope limitations.

## Release evidence

Every release must include:
- Version and exact commit SHA.
- CI run URL(s) and test scope.
- Review/approval reference.
- Adoption status for each supported profile.
- Known limitations and unresolved non-blocking issues.
- Licensing notice and applicable reuse terms.

## No implied certification

NUEGS defines governance requirements and validation tools. It does not, by itself, grant legal compliance, security certification, standards conformity, production readiness, or authorization to execute protected actions. Each claim must be scoped to a target and supported by current evidence.
