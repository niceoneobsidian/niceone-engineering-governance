import json, subprocess, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class ProfileTests(unittest.TestCase):
    def test_profiles_resolve(self):
        for name in ("niceone-obsidian","ai-agents"):
            result=subprocess.run([sys.executable,str(ROOT/"tooling/resolve_profile.py"),name],capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stdout+result.stderr)
            self.assertEqual(json.loads(result.stdout)["unresolved_domains"],[])
    def test_unknown_profile_fails(self):
        result=subprocess.run([sys.executable,str(ROOT/"tooling/resolve_profile.py"),"unknown"],capture_output=True,text=True)
        self.assertNotEqual(result.returncode,0)
if __name__=="__main__": unittest.main()
