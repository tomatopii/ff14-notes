#!/usr/bin/env python3
"""公式ジョブガイド（jp.finalfantasyxiv.com/jobguide/scholar/）からアクション名・Lv・アイコンを取り直して actions.json を作る。
一般アクション（LB・追従・移動・強化薬・食事）は xivapi から general_icons.json へ。"""
import re, json, html, base64, io, subprocess, pathlib, urllib.request
from PIL import Image
here = pathlib.Path(__file__).parent
src = urllib.request.urlopen("https://jp.finalfantasyxiv.com/jobguide/scholar/").read().decode("utf-8")
out = []
for r in re.finditer(r'<tr id="([^"]+)"(.*?)</tr>', src, flags=re.S):
    tid, body = r.group(1), r.group(2)
    if not (tid.startswith("pve_action__") or tid.startswith("healer_action__") or tid.startswith("pvp")): continue
    if "trait" in tid: continue
    img = re.search(r'(https://lds-img[^"]+\.png)', body); name = re.search(r"<strong>(.*?)</strong>", body, flags=re.S)
    if not (img and name): continue
    n = html.unescape(re.sub("<.*?>", "", re.sub(r"<rt>.*?</rt>", "", name.group(1), flags=re.S))).strip()
    lv = re.search(r"Lv\.?\s*(\d+)|レベル\s*(\d+)", re.sub("<.*?>", " ", body)); lvv = (lv.group(1) or lv.group(2)) if lv else ""
    out.append({"id": tid, "name": n, "lv": lvv, "url": img.group(1)})
seen = set(); o2 = []
for o in out:
    if o["id"] in seen and o["id"].startswith("healer"): continue
    seen.add(o["id"]); o2.append(o)
def b64(data):
    im = Image.open(io.BytesIO(data)).convert("RGBA").resize((48, 48), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, "PNG", optimize=True); return "data:image/png;base64," + base64.b64encode(b.getvalue()).decode()
for o in o2: o["b64"] = b64(urllib.request.urlopen(o["url"]).read())
(here / "actions.json").write_text(json.dumps(o2, ensure_ascii=False), encoding="utf-8")
GEN = {"lb": "000000/000103", "heel": "000000/000529", "pmove": "000000/000527", "tincture": "020000/020708", "food": "024000/024162"}
gen = {k: b64(urllib.request.urlopen(f"https://beta.xivapi.com/api/1/asset?path=ui/icon/{p}_hr1.tex&format=png").read()) for k, p in GEN.items()}
(here / "general_icons.json").write_text(json.dumps(gen), encoding="utf-8")
print(len(o2), "actions")
