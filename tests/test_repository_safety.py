"""Guard the published plugin instructions against the former direct-main exception."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "ascend-gtm-operator"


class RepositorySafetyTests(unittest.TestCase):
    def test_operator_requires_branch_and_forbids_direct_main(self):
        context = (PLUGIN / "context" / "OPERATOR.md").read_text()
        self.assertIn("dedicated feature branch", context)
        self.assertIn("Never commit or push directly to main", context)
        self.assertIn("including through a GitHub connector", context)

    def test_no_affirmative_direct_main_exception_in_plugin_docs(self):
        # Catch the removed wording and common equivalent exceptions, including
        # wrapped lines. Negative prohibitions are checked separately above.
        pattern = re.compile(
            r"(?:exception|allowed|fine|may|can|permit)[^.\n]{0,160}"
            r"(?:commit|push)[^.\n]{0,80}(?:directly )?to main",
            re.IGNORECASE,
        )
        for path in PLUGIN.rglob("*.md"):
            text = re.sub(r"(?<!\n)\n(?!\n)", " ", path.read_text())
            self.assertIsNone(pattern.search(text), str(path))


if __name__ == "__main__":
    unittest.main()
