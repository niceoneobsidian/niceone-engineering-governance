#!/usr/bin/env python3
"""Reference policy evaluator; this is not a trusted enforcement service."""
import argparse, json
ORDER = {"R0":0,"R1":1,"R2":2,"R3":3,"R4":4}
PROTECTED = {"protected_write","production_deploy","secret_rotation","destructive_delete","permission_change","external_publish"}
def evaluate(profile, action, risk, authorized=False, approval=False):
    if profile not in {"niceone-obsidian","ai-agents"}: return {"decision":"deny","reason":"unknown profile"}
    if risk not in ORDER: return {"decision":"deny","reason":"unknown risk class"}
    if action in PROTECTED and not authorized: return {"decision":"deny","reason":"protected action requires explicit authorization"}
    if ORDER[risk] >= 3 and not approval: return {"decision":"deny","reason":"R3/R4 requires explicit approval"}
    return {"decision":"allow_within_specification","reason":"no denial triggered; external enforcement still required"}
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--profile",required=True,choices=["niceone-obsidian","ai-agents"])
    p.add_argument("--action",required=True); p.add_argument("--risk",required=True,choices=list(ORDER))
    p.add_argument("--authorized",action="store_true"); p.add_argument("--approval",action="store_true")
    a=p.parse_args(); result=evaluate(a.profile,a.action,a.risk,a.authorized,a.approval); print(json.dumps(result,indent=2))
    return 0 if result["decision"]=="allow_within_specification" else 1
if __name__ == "__main__": raise SystemExit(main())
