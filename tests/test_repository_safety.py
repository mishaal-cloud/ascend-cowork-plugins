"""Guard distributed instructions against affirmative direct-main guidance."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "ascend-gtm-operator"

# Split clauses so a prohibition cannot hide an affirmative instruction later in
# the sentence. Normalize wrapped Markdown before looking for instructions.
CLAUSE = re.compile(r"[\n.;!?]+")
DIRECT_MAIN = re.compile(
    r"\b(?:git\s+push\s+(?:--\S+\s+)*\S+\s+main\b|"
    r"(?:commit(?:s|ted|ting)?|push(?:es|ed|ing)?)\b[^;.!?\n]{0,100}?"
    r"\b(?:to|on|into)\s+(?:the\s+)?(?:`)?main\b)", re.I
)
PROHIBITION = re.compile(
    r"\b(?:never|do not|don't|must not|cannot|can't|prohibit(?:ed)?|forbid(?:den)?)\b", re.I
)


def unsafe_direct_main(text):
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
    for clause in CLAUSE.split(text):
        match = DIRECT_MAIN.search(clause)
        if match and not PROHIBITION.search(clause[:match.start()]):
            suffix = clause[match.end():]
            if not re.match(r"\s+(?:is|are)\s+(?:prohibited|forbidden|not allowed)\b", suffix, re.I):
                return match.group()
    return None


class RepositorySafetyTests(unittest.TestCase):
    def test_operator_requires_branch_and_forbids_direct_main(self):
        context = (PLUGIN / "context" / "OPERATOR.md").read_text()
        self.assertIn("dedicated feature branch", context)
        self.assertIn("Never commit or push directly to main", context)
        self.assertIn("including through a GitHub connector", context)

    def test_scanner_rejects_affirmative_instructions(self):
        examples = (
            "Exception: small website edits are fine here via the GitHub connector (commit to main on `mishaal-cloud/ascendgtm-site`).",
            "Run `git push origin main`.",
            "Commit directly to main.",
            "You may commit changes on main.",
            "Pushing to main is allowed.",
            "Never push to main; git push origin main",
        )
        for example in examples:
            with self.subTest(example=example):
                self.assertIsNotNone(unsafe_direct_main(example))

    def test_scanner_accepts_prohibitions(self):
        for example in ("Never commit or push directly to main.",
                        "Do not run git push origin main.",
                        "Pushing to main is prohibited."):
            with self.subTest(example=example):
                self.assertIsNone(unsafe_direct_main(example))

    def test_no_affirmative_direct_main_in_distributed_instructions(self):
        for path in [ROOT / "README.md", *PLUGIN.rglob("*.md"), *PLUGIN.rglob("*.json")]:
            with self.subTest(path=path):
                self.assertIsNone(unsafe_direct_main(path.read_text()))

    def test_claude_manifest_version(self):
        manifest = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text())
        self.assertEqual(manifest["version"], "1.3.1")


if __name__ == "__main__":
    unittest.main()
