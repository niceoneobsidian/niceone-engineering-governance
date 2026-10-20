# Risk Classification

| Class | Description | Minimum controls |
|---|---|---|
| R0 | Read-only, reversible, low impact | Scope check; no sensitive-data exposure |
| R1 | Local, low-blast-radius changes | Diff review and relevant tests |
| R2 | Cross-module, integration or moderate data impact | Plan, risk-based tests, review where feasible, rollback plan |
| R3 | Production, sensitive data, privileged access or material external side effects | Explicit authorization, independent approval, staged execution, monitoring, recovery plan, evidence |
| R4 | Irreversible/destructive action or severe security/legal/safety impact | Default deny, named action-specific approval, independent verification, controlled window and tested recovery |

Consider impact, blast radius, reversibility, privilege, data sensitivity, external side effects, uncertainty and detectability. When uncertain, use the higher plausible class. Risk classification does not grant permission. R3/R4 actions require enforcement outside the prompt.
