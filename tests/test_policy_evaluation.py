import importlib.util, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("policy",ROOT/"tooling/evaluate_policy.py")
policy=importlib.util.module_from_spec(spec); spec.loader.exec_module(policy)
class PolicyTests(unittest.TestCase):
    def test_protected_action_denied_without_authorization(self):
        self.assertEqual(policy.evaluate("ai-agents","protected_write","R1")["decision"],"deny")
    def test_high_risk_denied_without_approval(self):
        self.assertEqual(policy.evaluate("niceone-obsidian","read","R3",authorized=True)["decision"],"deny")
    def test_routine_action_allowed_within_spec(self):
        self.assertEqual(policy.evaluate("ai-agents","read","R0")["decision"],"allow_within_specification")
    def test_unknown_profile_denied(self):
        self.assertEqual(policy.evaluate("unknown","read","R0")["decision"],"deny")
if __name__=="__main__": unittest.main()
