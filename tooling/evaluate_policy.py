#!/usr/bin/env python3
"""Reference policy evaluator; never use this as a trusted authorization service."""
import argparse
import json

ORDER = {"R0": 0, "R1": 1, "R2": 2, "R3": 3, "R4": 4}
PROTECTED = {
    "protected_write", "production_deploy", "secret_rotation",
    "destructive_delete", "permission_change", "external_publish",
}
KNOWN_ACTIONS = {"read", "propose", "local_write", "run_check"} | PROTECTED


def evaluate(profile, action, risk, authorized=False, approval=False):
    """Return a conservative reference decision from caller-supplied booleans.

    The booleans are not cryptographic, scoped, expiring authorization records.
    A trusted runtime must independently authorize actor/action/resource/scope.
    """
    if profile not in {"niceone-obsidian", "ai-agents"}:
        return {"decision": "deny", "reason": "unknown profile"}
    if risk not in ORDER:
        return {"decision": "deny", "reason": "unknown risk class"}
    if action not in KNOWN_ACTIONS:
        return {"decision": "deny", "reason": "unknown action"}
    if action in PROTECTED and not authorized:
        return {"decision": "deny", "reason": "protected action requires explicit authorization"}
    if action in PROTECTED and not approval:
        return {"decision": "deny", "reason": "protected action requires explicit approval"}
    if ORDER[risk] >= 3 and not approval:
        return {"decision": "deny", "reason": "R3/R4 requires explicit approval"}
    return {
        "decision": "allow_within_specification",
        "reason": "no denial triggered; trusted external enforcement is still required",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", required=True, choices=["niceone-obsidian", "ai-agents"])
    parser.add_argument("--action", required=True)
    parser.add_argument("--risk", required=True, choices=list(ORDER))
    parser.add_argument("--authorized", action="store_true")
    parser.add_argument("--approval", action="store_true")
    args = parser.parse_args()
    result = evaluate(args.profile, args.action, args.risk, args.authorized, args.approval)
    print(json.dumps(result, indent=2))
    return 0 if result["decision"] == "allow_within_specification" else 1


if __name__ == "__main__":
    raise SystemExit(main())
