#!/usr/bin/env python3
"""Validate NUEGS registries and cross-references using only the Python standard library."""
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
    "schemas/profile.schema.json", "schemas/standards.schema.json",
    "schemas/evidence.schema.json", "controls/policy-schema.json",
    "metrics/metric-schema.json",
]
VALID_RISKS = {"R0", "R1", "R2", "R3", "R4"}
PROFILE_IDS = {"niceone-obsidian", "ai-agents"}
CONTROL_STATUSES = {"proposed", "defined", "implemented", "tested", "verified", "adopted", "deprecated", "superseded"}
STANDARD_STATUSES = {"verified_source", "candidate", "superseded", "withdrawn", "unavailable_to_verify"}
MAPPING_STATUSES = {"not_assessed", "partial", "mapped", "assessed"}
ENFORCEMENT_STATUSES = {"not_verified", "implemented", "tested", "verified", "adopted", "not_applicable"}


def load(rel):
    try:
        return json.loads((ROOT / rel).read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValueError(f"{rel}: {exc}") from exc


def unique_ids(rows, label, errors):
    seen = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            errors.append(f"{label}[{index}]: expected object")
            continue
        ident = row.get("id")
        if not isinstance(ident, str) or not ident.strip():
            errors.append(f"{label}[{index}]: missing string id")
        elif ident in seen:
            errors.append(f"{label}: duplicate ID {ident}")
        else:
            seen.add(ident)
    return seen


def validate():
    errors = [f"missing file: {p}" for p in REQUIRED if not (ROOT / p).is_file()]
    if errors:
        return errors

    try:
        standards = load("standards/standards-registry.yaml")
        domains = load("domains/domain-registry.yaml")
        controls = load("controls/control-registry.yaml")
        enforcement = load("controls/enforcement-map.yaml")
        metrics = load("metrics/metrics-registry.yaml")
        for name, rows in (("standards", standards), ("domains", domains),
                           ("controls", controls), ("enforcement map", enforcement),
                           ("metrics", metrics)):
            if not isinstance(rows, list):
                errors.append(f"{name}: expected list")
        if errors:
            return errors

        unique_ids(standards, "standards", errors)
        domain_ids = unique_ids(domains, "domains", errors)
        control_ids = unique_ids(controls, "controls", errors)
        unique_ids(enforcement, "enforcement map", errors)
        unique_ids(metrics, "metrics", errors)

        if len(domains) != 20:
            errors.append(f"expected 20 domains, found {len(domains)}")

        domain_slugs = set()
        for domain in domains:
            slug = domain.get("slug")
            if not isinstance(slug, str) or not slug:
                errors.append(f"{domain.get('id')}: missing domain slug")
                continue
            if slug in domain_slugs:
                errors.append(f"duplicate domain slug {slug}")
            domain_slugs.add(slug)
            rel = domain.get("profile_path", "")
            target = (ROOT / rel).resolve()
            if not target.is_relative_to(ROOT) or not target.is_file():
                errors.append(f"{domain.get('id')}: missing/unsafe domain profile path {rel}")
            if not isinstance(domain.get("applies_to"), list) or not set(domain["applies_to"]).issubset(PROFILE_IDS):
                errors.append(f"{domain.get('id')}: invalid applies_to profiles")

        for row in standards:
            ident = row.get("id", "<missing>")
            if not all(isinstance(row.get(k), str) and row[k].strip() for k in ("publisher", "title", "source_url")):
                errors.append(f"{ident}: publisher, title and source_url are required")
            if not str(row.get("source_url", "")).startswith("https://"):
                errors.append(f"{ident}: source URL must use HTTPS")
            if row.get("status") not in STANDARD_STATUSES:
                errors.append(f"{ident}: invalid standard status")
            if row.get("mapping_status") not in MAPPING_STATUSES:
                errors.append(f"{ident}: invalid mapping_status")

        for row in controls:
            ident = row.get("id", "<missing>")
            if row.get("status") not in CONTROL_STATUSES:
                errors.append(f"{ident}: invalid control status")
            if row.get("risk_min") not in VALID_RISKS:
                errors.append(f"{ident}: invalid risk")
            if not isinstance(row.get("evidence"), list) or not row["evidence"]:
                errors.append(f"{ident}: missing evidence requirements")
            if not isinstance(row.get("applies_to"), list) or not set(row["applies_to"]).issubset(PROFILE_IDS):
                errors.append(f"{ident}: invalid applies_to profiles")
            for field in ("title", "owner", "requirement", "verification"):
                if not isinstance(row.get(field), str) or not row[field].strip():
                    errors.append(f"{ident}: missing {field}")

        for row in enforcement:
            ident = row.get("id", "<missing>")
            target_control = row.get("control")
            if target_control not in control_ids:
                errors.append(f"{ident}: references unknown control {target_control}")
            if row.get("status") not in ENFORCEMENT_STATUSES:
                errors.append(f"{ident}: invalid enforcement status")
            if not isinstance(row.get("evidence_required"), list) or not row["evidence_required"]:
                errors.append(f"{ident}: missing evidence_required")
            for field in ("target", "enforcement_point", "mode"):
                if not isinstance(row.get(field), str) or not row[field].strip():
                    errors.append(f"{ident}: missing {field}")

        for row in metrics:
            ident = row.get("id", "<missing>")
            if row.get("profile") not in PROFILE_IDS | {"shared"}:
                errors.append(f"{ident}: invalid metric profile")
            for field in ("name", "unit", "definition", "source", "cadence"):
                if not isinstance(row.get(field), str) or not row[field].strip():
                    errors.append(f"{ident}: missing {field}")
            if row.get("direction") not in {"lower_is_better", "higher_is_better", "contextual"}:
                errors.append(f"{ident}: invalid metric direction")

        all_gate_ids = set()
        for rel in ("profiles/niceone-obsidian/profile.yaml", "profiles/ai-agents/profile.yaml"):
            profile = load(rel)
            if profile.get("id") not in PROFILE_IDS:
                errors.append(f"{rel}: invalid profile id")
            if profile.get("status") not in {"proposed", "defined", "implemented", "tested", "verified", "adopted", "deprecated"}:
                errors.append(f"{rel}: invalid profile status")
            required_domains = profile.get("required_domains", [])
            if not isinstance(required_domains, list) or not set(required_domains).issubset(domain_slugs):
                errors.append(f"{rel}: references unknown domain")
            gates_rel = str(Path(rel).parent / profile.get("acceptance_gates", ""))
            gates = load(gates_rel)
            if not isinstance(gates, list):
                errors.append(f"{gates_rel}: expected list")
                continue
            for gate in gates:
                ident = gate.get("id", "<missing>")
                if ident in all_gate_ids:
                    errors.append(f"duplicate acceptance gate ID {ident}")
                all_gate_ids.add(ident)
                if gate.get("risk_min") not in VALID_RISKS or not isinstance(gate.get("evidence"), list) or not gate["evidence"]:
                    errors.append(f"{gates_rel}: malformed gate {ident}")
                if not gate.get("acceptance"):
                    errors.append(f"{gates_rel}: missing acceptance criteria for {ident}")

        for rel in ("schemas/profile.schema.json", "schemas/standards.schema.json",
                    "schemas/evidence.schema.json", "controls/policy-schema.json",
                    "metrics/metric-schema.json"):
            schema = load(rel)
            if not isinstance(schema, dict) or "$schema" not in schema or "type" not in schema:
                errors.append(f"{rel}: missing JSON Schema metadata")

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
