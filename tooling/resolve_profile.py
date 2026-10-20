#!/usr/bin/env python3
"""Resolve profile and required engineering domains."""
import json
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def main():
    if len(sys.argv) != 2 or sys.argv[1] not in {"niceone-obsidian","ai-agents"}:
        print("Usage: python tooling/resolve_profile.py <niceone-obsidian|ai-agents>", file=sys.stderr); return 2
    ident = sys.argv[1]
    profile = json.loads((ROOT/"profiles"/ident/"profile.yaml").read_text())
    domains = json.loads((ROOT/"domains/domain-registry.yaml").read_text())
    index = {d["slug"]:d for d in domains}
    missing = [slug for slug in profile.get("required_domains",[]) if slug not in index]
    result = {"profile":ident,"status":profile["status"],"required_domains":[index[s] for s in profile.get("required_domains",[]) if s in index],"unresolved_domains":missing}
    print(json.dumps(result,indent=2))
    return 1 if missing else 0
if __name__ == "__main__":
    raise SystemExit(main())
