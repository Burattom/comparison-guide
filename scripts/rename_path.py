import pathlib

OLD = "osechi-guide"
NEW = "comparison-guide"

for p in list(pathlib.Path(".").rglob("*.html")) + list(pathlib.Path(".").rglob("*.md")) + list(pathlib.Path(".").rglob("*.xml")) + list(pathlib.Path(".").rglob("*.txt")):
    if ".git" in p.parts:
        continue
    s = p.read_text(encoding="utf-8")
    if OLD not in s:
        continue
    p.write_text(s.replace(OLD, NEW), encoding="utf-8")
    print("updated", p)
