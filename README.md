# ff14-notes

FF14（学者メイン、Razer Naga 12ボタンマウス）の個人メモ。

## 中身

| パス | 何 |
| --- | --- |
| `hotbar/index.html` | ホットバーシミュレーター。ブラウザで開くだけで動く（単一ファイル、アイコン埋め込み済み） |
| `hotbar/template.html` | シミュレーターのソース（`__ICONS__` / `__GEN__` にデータを差し込む） |
| `hotbar/actions.json` | 公式ジョブガイドから取ったアクション名・Lv・アイコン（base64） |
| `hotbar/general_icons.json` | LB・追従・移動・強化薬・食事のアイコン |
| `hotbar/build.py` | template + json → index.html |
| `hotbar/fetch_icons.py` | 公式サイトからアイコンを取り直す（パッチでアクションが変わった時用） |
| `macros/FF14_macros.txt` | マクロ全文。ゲーム内に貼り付けて使う |
| `docs/*.md` | ドキュメント（Claude Docs からの書き出し） |
| `docs/html/` | 同じ内容の HTML 版（オフラインで読む用） |

## ホットバーシミュレーターの使い方

1. `hotbar/index.html` を開く
2. 左の一覧から枠へドラッグ。枠同士もドラッグで入れ替え。× かダブルクリックで空に
3. 「配置をテキストでコピー」で 4列×3段のテキストが出る
4. 配置はブラウザに自動保存される。「初期配置に戻す」でドキュメントの最終形に戻る

更新手順：`template.html` を編集 → `python3 hotbar/build.py` → `index.html` をコミット。

## ドキュメント

| ファイル | 内容 |
| --- | --- |
| `docs/00_index.md` | 索引 |
| `docs/01_naming.md` | キャラ・リテイナーの命名リスト |
| `docs/02_macros.md` | マクロ集（本文・書き方・テンプレ） |
| `docs/03_roadmap.md` | ロードマップ |
| `docs/04_events.md` | 開催中イベント（2026年10月） |
| `docs/05_settings.md` | 設定・ギアセット・ホットバー配置・キー割り当て・日次週次 |
| `docs/06_irreversible.md` | 取り返しのつかない要素 |
| `docs/07_scholar_skills.md` | 学者スキルのリサーチ（Lv1〜100、置き換え、回し） |

アイコン画像は © SQUARE ENIX。個人用途。
