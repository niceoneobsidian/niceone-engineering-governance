# OIS Execution Policy

Workflow: `Discover → Classify Risk → Plan → Authorize → Execute → Validate → Record Evidence → Close or Recover`.

Deny protected actions when identity, scope, policy, approval, environment, state or evidence requirements are missing, invalid or expired. Fail closed on policy-engine errors. Risk classification does not grant permission.

Use least privilege, bounded inputs, timeouts and checkpoints. Validate postconditions independently of model assertions. Retry only when safe. Require explicit action-specific approval for production changes, destructive operations, broad access and exceptions.

Evidence should include task ID, actor, action, target, policy version, authorization reference, timestamps, result, validation and evidence links. Redact secrets and unnecessary personal data.
