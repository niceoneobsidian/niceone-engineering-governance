import importlib.util, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("registry",ROOT/"tooling/validate_registry.py")
registry=importlib.util.module_from_spec(spec); spec.loader.exec_module(registry)
class RegistryTests(unittest.TestCase):
    def test_registries_validate(self):
        self.assertEqual(registry.validate(),[])
if __name__=="__main__": unittest.main()
