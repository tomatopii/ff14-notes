#!/usr/bin/env python3
"""template.html + actions.json + general_icons.json -> index.html"""
import json, pathlib
here = pathlib.Path(__file__).parent
tpl = (here / "template.html").read_text(encoding="utf-8")
acts = json.loads((here / "actions.json").read_text(encoding="utf-8"))
slim = [{"id": a["id"], "name": a["name"], "b64": a["b64"]} for a in acts]
gen = json.loads((here / "general_icons.json").read_text(encoding="utf-8"))
out = tpl.replace("__ICONS__", json.dumps(slim, ensure_ascii=False)).replace("__GEN__", json.dumps(gen))
(here / "index.html").write_text(out, encoding="utf-8")
print("index.html", len(out) // 1024, "KB")
