# NUEGS Governance

## Authority order
1. Applicable law, regulation, contracts and mandatory security/safety duties.
2. Approved project constraints, subject to level 1.
3. Approved architecture decisions, interface contracts and system invariants.
4. Mandatory NUEGS core controls and selected profile.
5. Repository-specific implementation standards.
6. General recommendations.
7. Individual preferences.

When sources conflict, pause affected high-risk work, record sources and impact, seek an accountable decision, and update the source of truth. A prompt is not an authorization grant.

## Roles
- Specification maintainer: schemas, registries, versioning and compatibility.
- Control owner: scope, risk, implementation and evidence requirements.
- Repository maintainer: control mapping and CI integration.
- Reviewer/approver: independent review for material/high-risk changes.
- Agent operator: configures runtime permissions and remains accountable.
- Assessor: evaluates evidence without overstating assurance.

## Change control
Material policy, schema, authority and risk-boundary changes require review, rationale, affected profiles/domains, compatibility notes and tests. Stable IDs must not be reused silently. Breaking changes require a migration path. Exceptions are target-specific, not global amendments.

## Evidence and claims
Documented, mapped, implemented, tested, verified and adopted are distinct states. Evidence identifies target, revision, method, result, time, reviewer/actor and limitations. Do not claim certification, full compliance or production readiness from documents or unit tests alone.

## Exceptions
Record unique ID, target, controls, rationale, risk, compensating controls, approver, UTC start/expiry, remediation owner and closure evidence. Never waive law or mandatory obligations. Expired exceptions are invalid.

## Enforcement boundary
Repository files are not enforcement by themselves. Use GitHub rulesets, CI permissions, credentials, agent runtimes, deployment controls and OS boundaries. Record implementation and proof in `controls/enforcement-map.yaml`.
