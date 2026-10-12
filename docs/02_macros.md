# FF14 マクロ集

Oct 8, 2026 · @tomatopii

## 一覧（16個）

| 保存先 | 番号 | 名前 | 置き場所 |
| --- | --- | --- | --- |
| 共有 | 0 | 挨拶：入場 | Ctrl層 |
| 共有 | 1 | 挨拶：退場 | Ctrl層 |
| 共有 | 2 | 挨拶：謝罪 | Ctrl層 |
| 共有 | 3 | 挨拶：お礼 | Ctrl層 |
| 共有 | 10 | 切替：学者 | Ctrl層 |
| 共有 | 11 | 切替：モンク | Ctrl層 |
| 個別 | 0 | 学者：蘇生 | Alt層 |
| 個別 | 1 | 学者：エスナ | Alt層 |
| 個別 | 2 | 学者：鼓舞 | Alt層 |
| 個別 | 3 | 学者：生命活性 | Alt層 |
| 個別 | 4 | 学者：フィジク | Alt層 |
| 個別 | 5 | 学者：入場 | Ctrl層 |
| 個別 | 6 | 学者：陣 | 層1の9 |
| 個別 | 50 | PvP：鼓舞 | PvPバー 8 |
| 個別 | 51 | PvP：展開 | PvPバー 3 |
| 個別 | 52 | PvP：ヒール | PvPバー 11（FL/RWのみ） |

マウントルーレット・テレポ・デジョン・LB・スプリント・ポーションはマクロにせず直接ドラッグ。

## 共有

**0　挨拶：入場**

```
/macrolock
/macroicon "手を振る" emote
/macroerror off
/party よろしくお願いします！
/alliance よろしくお願いします！
/wave motion
```

**1　挨拶：退場**

```
/macrolock
/macroicon "お辞儀する" emote
/macroerror off
/party ありがとうございました！お疲れ様でした！
/alliance ありがとうございました！
/bow motion
```

**2　挨拶：謝罪**

```
/macrolock
/macroicon "ひざまずく" emote
/macroerror off
/party すみません、失礼しました。
/bow motion
```

**3　挨拶：お礼**

```
/macrolock
/macroicon "拍手する" emote
/macroerror off
/party ありがとうございます！
/clap motion
```

**10　切替：学者**

```
/macroicon 2 gearset
/macroerror off
/gearset change "学者"
/hudlayout 2
```

**11　切替：モンク**

```
/macroicon 1 gearset
/macroerror off
/gearset change "モンク"
/hudlayout 1
```

## 個別（学者）

**0　学者：蘇生**

```
/macrolock
/macroicon リザレク
/macroerror off
/action 迅速魔 <wait.1>
/action リザレク <mo>
/action リザレク <t>
/party リザレク → <t>
```

**1　学者：エスナ**

```
/macroicon エスナ
/macroerror off
/action エスナ <mo>
/action エスナ <t>
```

**2　学者：鼓舞**

```
/macroicon 鼓舞激励の策
/macroerror off
/action 鼓舞激励の策 <mo>
/action 鼓舞激励の策 <t>
/action 鼓舞激励の策 <2>
```

`<2>` はパーティリスト2番目（タンクを上に並べておく）。

**3　学者：生命活性**

```
/macroicon 生命活性法
/macroerror off
/action 生命活性法 <mo>
/action 生命活性法 <t>
```

**4　学者：フィジク**

```
/macroicon フィジク
/macroerror off
/action フィジク <mo>
/action フィジク <t>
```

**5　学者：入場**

```
/macrolock
/macroicon サモン・エオス
/macroerror off
/action サモン・エオス
/party よろしくお願いします！
/alliance よろしくお願いします！
/wave motion
```

**6　学者：陣**（マウス位置に即設置）

```
/macroicon 野戦治療の陣
/macroerror off
/action 野戦治療の陣 gtoff
/action 野戦治療の陣 <me>
```

`gtoff` は地面指定カーソルを出さず、マウスカーソルの位置にその場で設置（`< >` は付けない）。2行目はカーソルが届かない位置のときの保険で、自分の足元に置く。キャラクターコンフィグ → 操作設定 → ターゲット → グラウンドターゲット設定の「GTアクションの有効範囲内のみ操作可能にする」をオンにすると、カーソルが範囲外でも届く端に寄せて置いてくれる。

## 個別（学者 PvP）

PvP 専用アクションは `/action` ではなく `/pvpaction`、アイコンは `pvpaction` 型。PvP ホットバーは PvE と別セットなので、マクロをそちらに置く。

**50　PvP：鼓舞**

```
/macroicon 鼓舞激励の策 pvpaction
/macroerror off
/pvpaction 鼓舞激励の策 <mo>
/pvpaction 鼓舞激励の策 <t>
```

**51　PvP：展開**

```
/macroicon 展開戦術 pvpaction
/macroerror off
/pvpaction 展開戦術 <mo>
/pvpaction 展開戦術 <t>
```

**52　PvP：ヒール**（ロールアクション。フロントライン・ライバルウィングズで「ヒール」を選んだときだけ）

```
/macroicon ヒール pvpaction
/macroerror off
/pvpaction ヒール <mo>
/pvpaction ヒール <t>
```

快気・疾風怒濤・セラフィズムは自分対象、蚠毒法・楹炎法・連環計は敵対象なのでマクロ不要。

## テンプレ（スキル名を入れ替えるだけ）

**敵へのアクション**…マクロ不要。アクションをそのまま置く（ターゲットに飛ぶ。マクロにすると先行入力が死ぬ）

**自分へのアクション**…マクロ不要。そのまま置く

**味方単体へのアクション**（マウスオーバー→ターゲット→タンク）

```
/macroicon スキル名
/macroerror off
/action スキル名 <mo>
/action スキル名 <t>
/action スキル名 <2>
```

最後の `<2>` は「誰も指していないならパーティリスト2番目」。タンクに飛ばしたいスキル（鼓舞・深謀・エーテルパクト）にだけ付ける。回復・エスナ・救出は外す。

**蘇生**（迅速魔つき）

```
/macrolock
/macroicon リザレク
/macroerror off
/action 迅速魔 <wait.1>
/action リザレク <mo>
/action リザレク <t>
/party リザレク → <t>
```

**パーティ番号指定**（N は 1〜8。`<1>` は自分）

```
/macroicon スキル名
/action スキル名 <N>
```

当てはめるスキル（味方単体を対象にするものだけ）：フィジク・エスナ・リザレク・鼓舞激励の策・生命活性法・救出(48)・展開戦術(56)・深謀遠慮の策(62)・エーテルパクト(70)・生命回生法(86)

## 書き方

- 15行、1行180文字。上から順に実行、失敗した行は飛ばす（`<mo>`→`<t>` の二段構えはこれを利用）
- マクロは先行入力が効かない。連打するGCDはマクロにしない
- 挨拶は通常の文字でOK（貼り付けそのまま動く）。海外の人と組むなら、マクロ編集画面で文言を消して **Tab** → 定型文辞書（自動翻訳）から選ぶ。`{ }` を文字で貼っても翻訳されない
- `/micon 2 gearset` の数字はギアセット一覧の並び順

| コマンド（省略形） | 意味 |
| --- | --- |
| `/action`（`/ac`） | アクション実行 |
| `/pvpaction`（`/pvpac`） | PvPアクション実行（PvPエリア専用） |
| `/macroicon`（`/micon`） | アイコン |
| `/macrolock`（`/mlock`） | 実行中、他のマクロを割り込ませない |
| `/macroerror off`（`/merror`） | 失敗行のエラーを非表示（マクロ終了で自動復帰） |
| `/party`（`/p`）`/alliance`（`/a`） | パーティ／アライアンスチャット |
| `/エモート motion` | 動作だけ。ログに定型セリフを出さない |
| `<wait.n>` | n秒待つ（整数、最大60） |

**`/macroicon "名前" 種類`**

| 種類 | 対象 |
| --- | --- |
| （省略） | アクション |
| general | 汎用アクション（テレポ・LB・マウントルーレット） |
| emote | エモート。エモートリストの表示名（手を振る・お辞儀する・ひざまずく） |
| item | アイテム（所持数表示） |
| mount / minion | マウント／ミニオン |
| gearset | ギアセット番号 |
| classjob | ジョブ名 |
| pet / buddy | 妖精／バディのアクション |
| marking / waymark | マーキング／フィールドマーカー |

アイコンが「M」のまま：名前の完全一致・種類・`" "` の3つを確認。

**ターゲット指定子**

| 指定子 | 対象 |
| --- | --- |
| `<t>` | ターゲット |
| `<mo>` | マウスオーバー（パーティリスト上） |
| `<me>` | 自分 |
| `<tt>` | ターゲットのターゲット |
| `<1>`〜`<8>` | パーティリストの番号 |
| `<f>` | フォーカスターゲット |

出典：[/macroicon](https://jp.finalfantasyxiv.com/lodestone/playguide/db/text_command/e6e219e1adc/)、[マクロ専用コマンド](https://jp.finalfantasyxiv.com/lodestone/playguide/db/text_command/?category2=7)、[エモートコマンド](https://jp.finalfantasyxiv.com/lodestone/playguide/db/text_command/?category2=9)
