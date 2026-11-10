#!/usr/bin/env python3
"""Backfill du champ `resume` (condensé 2-3 lignes) dans le frontmatter de toutes
les skills/*.md. Le resume est dérivé du corps (Objectif + étape 1) via
routage.resume_auto — déterministe, identique au build canvas et --from-skills.
Usage : python3 outils/backfill_resume.py [--check]
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from routage import resume_auto  # noqa: E402

SK = Path(__file__).resolve().parent.parent / "skills"


def main() -> int:
    check = "--check" in sys.argv
    n = 0
    for f in sorted(SK.glob("*.md")):
        txt = f.read_text(encoding="utf-8")
        m = re.match(r"---\n(.*?)\n---\n", txt, re.S)
        assert m, f"{f.name} : pas de frontmatter"
        fm = m.group(1)
        mr = re.search(r'^resume: "(.*)"$', fm, re.M)
        body = txt[m.end():]
        attendu = resume_auto(body)
        if mr:
            if mr.group(1) != attendu and check:
                print(f"  ~ {f.name} : resume présent mais différent du dérivé")
            continue
        assert '"' not in attendu and "<" not in attendu and ">" not in attendu, f.name
        if check:
            print(f"  + {f.name} : resume manquerait")
            n += 1
            continue
        new_fm = re.sub(r"^(num: \d+\n)", rf'\1resume: "{attendu}"\n', fm, count=1, flags=re.M)
        assert new_fm != fm, f.name
        f.write_text(f"---\n{new_fm}\n---\n{body}", encoding="utf-8")
        n += 1
    print(f"✅ resume {'à ajouter' if check else 'ajouté'} à {n} fichiers sur {len(list(SK.glob('*.md')))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
