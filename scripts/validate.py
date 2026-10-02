"""Check the distributable skill and its observable seed-script contract."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
from urllib.parse import unquote

import yaml


workspace = Path(__file__).resolve().parents[1]
package = workspace / "skills" / "ui-product-design"
files = sorted(path for path in package.rglob("*") if path.is_file())
snapshot = {}
link_count = 0
for path in files:
    snapshot[path.relative_to(package).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    if path.suffix in {".md", ".yaml", ".yml", ".ps1", ".py", ".txt"} or path.name == "LICENSE":
        content = path.read_text(encoding="utf-8")
        if "\ufffd" in content:
            raise AssertionError(f"Replacement character in {path}")

markdown = {workspace / "README.md", workspace / "CONTRIBUTING.md"}
for folder in ("docs", "examples", "skills"):
    markdown.update((workspace / folder).rglob("*.md"))
for path in sorted(markdown):
    for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
        if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
            continue
        resolved = path.parent / unquote(target.split("#", 1)[0])
        if not resolved.exists():
            raise AssertionError(f"Broken local link in {path}: {target}")
        link_count += 1

entry = (package / "SKILL.md").read_text(encoding="utf-8")
frontmatter = yaml.safe_load(entry.split("---", 2)[1])
assert frontmatter["name"] == package.name
assert isinstance(frontmatter["description"], str) and frontmatter["description"]
assert frontmatter["license"] == "MIT"
assert (package / "LICENSE").read_bytes() == (workspace / "LICENSE").read_bytes()
metadata = yaml.safe_load((package / "agents" / "openai.yaml").read_text(encoding="utf-8"))
assert 25 <= len(metadata["interface"]["short_description"]) <= 64
assert "$ui-product-design" in metadata["interface"]["default_prompt"]
assert metadata.get("policy", {}).get("allow_implicit_invocation", True)

shell = shutil.which("pwsh") or shutil.which("powershell")
if not shell:
    raise RuntimeError("No PowerShell runtime available for the script check")
script = package / "scripts" / "new-design-seed.ps1"
observed = set()
for length in (32, 128, 512):
    for _ in range(3):
        result = subprocess.run(
            [shell, "-NoProfile", "-NonInteractive", "-File", str(script), "-Length", str(length)],
            capture_output=True, text=True, encoding="utf-8", errors="replace", check=True,
        )
        seed = result.stdout.strip()
        assert len(seed) == length and re.fullmatch(r"[A-Za-z0-9]+", seed)
        assert seed not in observed
        observed.add(seed)
        assert not result.stderr.strip(), result.stderr

for length in (31, 513):
    result = subprocess.run(
        [shell, "-NoProfile", "-NonInteractive", "-File", str(script), "-Length", str(length)],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    assert result.returncode != 0 and not result.stdout.strip(), "Invalid length was accepted"

review_prompt = package / "references" / "critic-prompt.md"
assert not re.search(r"(?:≥|>=|必须达到|门槛|停止条件)", review_prompt.read_text(encoding="utf-8"))
report = {
    "package": package.relative_to(workspace).as_posix(),
    "file_count": len(files),
    "local_links_checked": link_count,
    "valid_seed_invocations": len(observed),
    "invalid_lengths_rejected": [31, 513],
    "checks": "UTF-8, YAML, repository Markdown links, MIT license parity, invocation metadata, seed length/charset/uniqueness sample, invalid input exits",
    "limitations": "Samples do not statistically prove randomness; static checks do not prove design quality or platform acceptance.",
    "sha256": snapshot,
}
output = workspace / "build" / "validation.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(f"PASS: {len(files)} files, {link_count} local links, 9 seed calls, 2 rejected invalid lengths.")
