#!/usr/bin/env python3
"""Validate core NUEGS registries with only the Python standard library."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "standards/standards-registry.yaml", "domains/domain-registry.yaml",
    "controls/control-registry.yaml", "controls/enforcement-map.yaml",
    "metrics/metrics-registry.yaml", "profiles/niceone-obsidian/profile.yaml",
    "profiles/niceone-obsidian/acceptance-gates.yaml", "profiles/ai-agents/profile.yaml",
    "profiles/ai-agents/permission-model.yaml", "profiles/ai-agents/acceptance-gates.yaml",
]
def load(rel):
    try:
        return json.loads((ROOT / rel).read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValueError(f"{rel}: {exc}") from exc

def validate():
    errors = [f"missing file: {p}" for p in REQUIRED if not (ROOT / p).is_file()]
    if errors:
        return errors
    registries = [
        ("standards/standards-registry.yaml", "id"),
        ("domains/domain-registry.yaml", "id"),
        ("controls/control-registry.yaml", "id"),
        ("metrics/metrics-registry.yaml", "id"),
    ]
    ids = {}
    for rel, key in registries:
        try:
            rows = load(rel)
            if not isinstance(rows, list):
                errors.append(f"{rel}: expected list")
                continue
            for row in rows:
                ident = row.get(key)
                if not ident:
                    errors.append(f"{rel}: entry missing {key}")
                    continue
                if ident in ids:
                    errors.append(f"duplicate registry ID {ident}: {rel} and {ids[ident]}")
                ids[ident] = rel
                if rel == "controls/control-registry.yaml":
                    if row.get("risk_min") not in {"R0","R1","R2","R3","R4"}: errors.append(f"{ident}: invalid risk")
                    if not row.get("evidence"): errors.append(f"{ident}: missing evidence requirements")
                if rel == "standards/standards-registry.yaml" and not row.get("source_url","").startswith("https://"):
                    errors.append(f"{ident}: source URL must use HTTPS")
        except Exception as exc:
            errors.append(str(exc))
    try:
        domains = load("domains/domain-registry.yaml")
        if len(domains) != 20: errors.append(f"expected 20 domains, found {len(domains)}")
        slugs = set()
        for domain in domains:
            if domain["slug"] in slugs: errors.append(f"duplicate domain slug {domain['slug']}")
            slugs.add(domain["slug"])
            if not (ROOT / domain["profile_path"]).is_file(): errors.append(f"missing domain profile {domain['profile_path']}")
        for rel in ("profiles/niceone-obsidian/profile.yaml","profiles/ai-agents/profile.yaml"):
            profile = load(rel)
            if not set(profile.get("required_domains", [])).issubset(slugs):
                errors.append(f"{rel}: references unknown domain")
            gates = load(str(Path(rel).parent / profile["acceptance_gates"]))
            gate_ids = [g["id"] for g in gates]
            if len(gate_ids) != len(set(gate_ids)): errors.append(f"{rel}: duplicate gate IDs")
            for gate in gates:
                if gate.get("risk_min") not in {"R0","R1","R2","R3","R4"} or not gate.get("evidence"):
                    errors.append(f"{rel}: malformed gate {gate.get('id')}")
    except Exception as exc:
        errors.append(str(exc))
    return errors

if __name__ == "__main__":
    problems = validate()
    if problems:
        print("NUEGS validation FAILED")
        print("\n".join("- " + p for p in problems))
        sys.exit(1)
    print("NUEGS validation PASSED")
