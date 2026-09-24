import re
import subprocess
import unittest
from pathlib import Path
from urllib.parse import urldefrag

ROOT = Path(__file__).resolve().parents[1]
HTML_PAGES = sorted(
    path for path in ROOT.rglob("*.html")
    if ".git" not in path.parts and "src" not in path.relative_to(ROOT).parts
)

HREF_RE = re.compile(r'\b(?:href|src)="([^"]+)"')
ID_RE = re.compile(r'\bid="([^"]+)"')


def is_external(target: str) -> bool:
    return (
        target.startswith("http://")
        or target.startswith("https://")
        or target.startswith("mailto:")
        or target.startswith("data:")
        or target.startswith("tel:")
        or target.startswith("javascript:")
    )


class SiteContractTests(unittest.TestCase):
    def test_generated_pages_are_reproducible(self):
        before = {path: path.read_text(encoding="utf-8") for path in HTML_PAGES}

        subprocess.run(["python3", "build_features.py"], cwd=ROOT, check=True)
        subprocess.run(["python3", "build_pages.py"], cwd=ROOT, check=True)

        after = {path: path.read_text(encoding="utf-8") for path in HTML_PAGES}
        self.assertEqual(before, after)

    def test_internal_links_and_assets_resolve(self):
        self.assertGreaterEqual(len(HTML_PAGES), 8)
        for page in HTML_PAGES:
            html = page.read_text(encoding="utf-8")
            anchors = set(ID_RE.findall(html))
            for raw_target in HREF_RE.findall(html):
                if not raw_target or is_external(raw_target):
                    continue

                path_part, fragment = urldefrag(raw_target)
                if not path_part:
                    if fragment:
                        self.assertIn(fragment, anchors, f"{page} has broken same-page anchor {raw_target}")
                    continue

                resolved = (page.parent / path_part).resolve()
                try:
                    resolved.relative_to(ROOT)
                except ValueError:
                    self.fail(f"{page} links outside the repository: {raw_target}")

                self.assertTrue(resolved.exists(), f"{page} has broken local link or asset: {raw_target}")
                if fragment and resolved.suffix == ".html":
                    target_html = resolved.read_text(encoding="utf-8")
                    target_anchors = set(ID_RE.findall(target_html))
                    self.assertIn(fragment, target_anchors, f"{page} has broken anchor {raw_target}")

    def test_repository_contract_files_exist(self):
        self.assertTrue((ROOT / "LICENSE").is_file())
        self.assertTrue((ROOT / ".github/workflows/validate.yml").is_file())

    def test_builder_docs_match_current_entrypoints(self):
        build_py = (ROOT / "build.py").read_text(encoding="utf-8")
        self.assertNotIn("src/pages", build_py)
        self.assertNotIn("build_all.py", build_py)
        self.assertIn("build_features.py", build_py)
        self.assertIn("build_pages.py", build_py)

    def test_waitlist_copy_matches_email_only_signup_state(self):
        waitlist_html = (ROOT / "waitlist.html").read_text(encoding="utf-8")
        waitlist_source = (ROOT / "build_pages.py").read_text(encoding="utf-8")

        self.assertIn("Email to join the waitlist", waitlist_html)
        self.assertIn("Signup form is coming very soon", waitlist_html)
        self.assertNotIn("Fill out the form below", waitlist_html)
        self.assertNotIn("You submit the form", waitlist_html)
        self.assertNotIn("Downloads/pace-google-form-setup.md", waitlist_source)


if __name__ == "__main__":
    unittest.main()
