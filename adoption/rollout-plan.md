# NUEGS Adoption and Rollout Plan

## Phase 0 — Trusted baseline (P0)
Inspect repository state before edits; triage secret-scan findings; verify server-side branch rules and required checks; fix non-portable standards paths; inventory CI, permissions, recovery and production evidence.
**Exit:** findings resolved or contained, enforcement evidenced, repository states recorded.

## Phase 1 — Specify core controls (P1)
Review authority, risk, lifecycle, exceptions, evidence, versioning and control ownership. Validate schemas/registries and verify standards metadata.
**Exit:** reviewed baseline, stable IDs and automated validation.

## Phase 2 — Pilot the two profiles (P1)
Map OIS architecture, authorization, state/recovery, security, observability, testing and release; map agent discovery, instruction hierarchy, scope, permissions, secrets, verification and reporting. Distinguish documented from verified controls.
**Exit:** implementation map, test plan and explicit gaps for each profile.

## Phase 3 — Enforce minimum controls (P1)
Run deterministic checks in CI; define offline, integration, infrastructure-dependent and production-acceptance test tiers; configure rulesets; add secret scanning and disposition procedures; pin third-party actions to reviewed immutable SHAs where practical.
**Exit:** platform-enforced checks and documented negative tests for bypass prevention.

## Phase 4 — Expand (P2)
Pilot on OIS and Agent Weave after inspecting their current states; extend to other repositories only after owner review. Track drift, exceptions and metric quality.
**Exit:** each adopted repository has an owner, selected profile, baseline audit, control map and review cadence.

Review exceptions and drift monthly; review standards and profiles quarterly and after material incidents.
