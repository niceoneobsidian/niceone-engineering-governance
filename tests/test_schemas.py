import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def load_json(relative_path):
    return json.loads((ROOT / relative_path).read_text(encoding="utf-8"))


class SchemaValidationTests(unittest.TestCase):
    def assert_valid_against(self, instance, schema_path):
        schema = load_json(schema_path)
        Draft202012Validator.check_schema(schema)
        errors = sorted(
            Draft202012Validator(schema).iter_errors(instance),
            key=lambda error: list(map(str, error.absolute_path)),
        )
        self.assertEqual(
            errors,
            [],
            "\\n".join(
                f"{list(error.absolute_path)}: {error.message}" for error in errors
            ),
        )

    def test_profile_documents_match_schema(self):
        for path in (
            "profiles/niceone-obsidian/profile.yaml",
            "profiles/ai-agents/profile.yaml",
        ):
            with self.subTest(path=path):
                self.assert_valid_against(load_json(path), "schemas/profile.schema.json")

    def test_standard_registry_entries_match_schema(self):
        for item in load_json("standards/standards-registry.yaml"):
            with self.subTest(standard=item["id"]):
                self.assert_valid_against(item, "schemas/standards.schema.json")

    def test_control_registry_entries_match_schema(self):
        for item in load_json("controls/control-registry.yaml"):
            with self.subTest(control=item["id"]):
                self.assert_valid_against(item, "controls/policy-schema.json")

    def test_metric_registry_entries_match_schema(self):
        for item in load_json("metrics/metrics-registry.yaml"):
            with self.subTest(metric=item["id"]):
                self.assert_valid_against(item, "metrics/metric-schema.json")

    def test_evidence_schema_accepts_valid_example(self):
        example = {
            "evidence_id": "EV-TEST-001",
            "control_id": "CORE-TEST-001",
            "target": "test-repository",
            "revision": "abc123",
            "method": "unit-test",
            "result": "passed",
            "observed_at": "2026-10-20T00:00:00Z",
            "review_status": "unreviewed",
            "artifact_refs": ["tests/test_schemas.py"],
            "limitations": "Schema fixture only; not production evidence.",
        }
        self.assert_valid_against(example, "schemas/evidence.schema.json")

    def test_evidence_schema_rejects_missing_required_fields(self):
        invalid = {"evidence_id": "EV-INVALID"}
        with self.assertRaises(AssertionError):
            self.assert_valid_against(invalid, "schemas/evidence.schema.json")


if __name__ == "__main__":
    unittest.main()
