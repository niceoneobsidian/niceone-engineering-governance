# Niceone Obsidian Architecture Profile

## Governing boundary
Reasoning and planning may propose actions. Policy, authorization, scoped execution, validation and recorded evidence determine what occurs. Model output is not permission.

## Logical responsibilities
- Control plane/kernel: lifecycle, policy decisions, task state and enforcement integration.
- Cognition/planning: goals, constraints and bounded plans.
- Registries: capabilities, agents, tools and workflows.
- Model gateway: provider selection, quotas, failure handling and data boundaries.
- Knowledge/memory: provenance, retention, access and retrieval.
- Execution runtime: scoped tools, checkpoints and idempotency.
- Validation/recovery: postconditions, compensation and safe resumption.
- Observability: operational evidence, failures, latency and resource use.
- Controlled learning: evaluation, review and approved updates.

These are logical responsibilities, not a mandate to split everything into services.

## Invariants
1. Protected actions require authorization from a trusted enforcement point.
2. Evidence links task, actor, tool, target, revision and outcome where applicable.
3. State transitions are validated; unsafe retries cannot duplicate side effects.
4. Failure or interruption ends in a known recoverable or blocked state.
5. Secrets are excluded from routine logs and evidence.
6. Production claims require acceptance and recovery evidence.
7. Use the existing OIS capability maturity lifecycle.
