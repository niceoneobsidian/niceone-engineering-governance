# OIS State and Recovery

Validate task/workflow state transitions and reject illegal transitions. Persist state changes atomically where possible; record what was requested, authorized, attempted and verified. Keep secrets out of snapshots and define retention.

Before retrying, determine whether a side effect occurred. Use idempotency keys/deduplication for external operations where possible. Do not retry destructive or non-idempotent actions without a recovery policy.

Recovery: stop dependent actions; inspect durable state and evidence; determine side-effect status; revalidate environment and authorization; resume, compensate, retry safely or block; verify postconditions; record outcome; add a regression test.

Test illegal transitions, partial writes, interruption, timeouts, duplicate delivery, stale authorization, tool failure and recovery failure. State untested scenarios.
