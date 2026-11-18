"""Check a BuddhistAI workshop repo: variants have a version, provenance records are valid, no test data is copied."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []
for skill in sorted(ROOT.glob("variants/*/SKILL.md")):
    text = skill.read_text(encoding="utf-8")
    if not re.search(r"^\s+version:\s*\d+\.\d+\.\d+\s*$", text, re.M):
        errors.append(f"{skill.relative_to(ROOT)}: needs metadata.version (semver)")
for rec in sorted(ROOT.glob("provenance/*.json")):
    try:
        d = json.loads(rec.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        errors.append(f"{rec.relative_to(ROOT)}: not valid JSON ({e})")
        continue
    if d.get("schema") != "buddhistai/provenance@1":
        errors.append(f"{rec.relative_to(ROOT)}: schema must be buddhistai/provenance@1")
    if rec.stem != "example" and d.get("run_id") != rec.stem:
        errors.append(f"{rec.relative_to(ROOT)}: run_id must match the file name")
for f in ROOT.rglob("test.jsonl"):
    if ".git" not in f.parts and "eval" not in f.parts:
        errors.append(f"{f.relative_to(ROOT)}: test data belongs in buddhist-benchmarks, not here")
print("\n".join(errors) or "OK")
sys.exit(1 if errors else 0)
