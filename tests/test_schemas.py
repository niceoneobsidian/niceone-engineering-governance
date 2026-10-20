import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class RegistrySyntaxTests(unittest.TestCase):
    def test_machine_readable_files_parse(self):
        paths=list(ROOT.rglob("*.yaml"))+list(ROOT.rglob("*.json"))
        self.assertGreaterEqual(len(paths),20)
        for path in paths:
            with self.subTest(path=path.relative_to(ROOT)):
                json.loads(path.read_text(encoding="utf-8"))
    def test_schemas_have_json_schema_marker(self):
        for name in ("profile.schema.json","standards.schema.json","evidence.schema.json"):
            data=json.loads((ROOT/"schemas"/name).read_text())
            self.assertIn("$schema",data)
if __name__=="__main__": unittest.main()
