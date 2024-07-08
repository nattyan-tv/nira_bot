# NIRA Bot

痒い所に手が届きそうで届かない Discord 用 BOT

## Common Setup

Docker(`docker-compose`)での実行と、通常の実行の2つの方法をサポートしています。

以下は共通項目です。

### File: `setting.json`

BOT の設定ファイルを、以下の表または`setting_temp.json`を参考にして、`setting.json`に記述します。

- 設定ファイルを追加した際の構成サンプル
  ```sh
  N:.
  \--nira_bot
     +--main.py
     \--setting.json
  ```

#### `setting.json`の設定項目について

| キー                | 内容                                                                              | 例                                           | 変数型        |
| ------------------- | --------------------------------------------------------------------------------- | -------------------------------------------- | ------------- |
| `tokens`-`nira_bot` | Bot のトークン入れ                                                                | `"abcdefniofwpajrjr92.f3h208hfi0iffhifhihi"` | str           |
| `py_admin`          | 再起動や Onami などの管理者コマンドを使用できるユーザーの DiscordID             | `[1234567989,987654321]`                     | list[int]     |
| `voicevox`          | VOICEVOX WebAPI の API キー (必須ではない)                                       | `["abcdefg1234","1234abcdef"]`               | list[str]     |
| `prefix`            | コマンドのプレフィックス                                                          | `"n!"`                                       | str           |
| `guild_ids`         | スラッシュコマンドを登録する GuildID。未指定で全サーバーに登録する。              | `[1234567989,987654321]`                     | list[int]    |
| `unload_cogs`       | cogs フォルダにある Python ファイルで、Cog として読み込まないファイルを指定する。 | `["yabai.py","tondemonai.py"]`               | list[str]     |
| `load_cogs`         | Debug モードで起動した際に読み込む Cog を指定する。                               | `["debug.py"]`                               | list[str]     |
| `translate`         | DeepL API のキー（必須ではない）                                                  | `abcd1234-ab12-ab12-ab12-ab12ab12ab12`       | str           |
| `database_url`      | MongoDB のデータベースのURL                                                  | `mongo+srv://test...`       | str |
| `database_name`     | MongoDB のデータベースの名前                                                  | `test`       | str |

### Running

なんにしろ、エントリーポイントは`main.py`です。

BOT を Debug モードで起動する場合は、引数として`-d`を指定します。  
Debug モードで起動すると、下記の状態になります。

- `setting.json`の`load_cogs`で指定された Cog のみが読み込まれます。
- 起動時に通常より少し多くのコンソール表示が行われます。
- Discord 上での BOT のステータス表記が変更されます。


## Build and Run with `docker-compose`

### Requirements

- 最低限のスペックとネットワークを兼ね備えた PC
- Docker, Docker Compose

### Setup and Run

1. `setting.json`を作成します。
2. 以下のコマンドまたは好きな方法でビルド、実行します。

```sh
$ docker-compose up --build
```
(このコマンドを実行すると、ビルドと実行が同時に行われます。)

## Build and Run with `normally`

### Requirements

- 最低限のスペックとネットワークを兼ね備えた PC (Windows/Linux/macOS)
- Python 3.10 以上

### Setup

1. `pip3 install -r requirements.txt`などの方法で、`requirements.txt`のモジュールをインストールします。
2. `setting.json`を作成します。
3. `main.py`を実行します。

# enhance-fix

もし、プログラムに不具合があったり、機能改善をしてほしい場合は、[にら BOT Discord サーバー](https://discord.gg/awfFpCYTcP)の`#enhance-fix`でスレッドを立てるか、本レポジトリに issue や PR を立ててください。

# Contribute

`develop`ブランチに対してPRを送っていただければ、レビューを行った上でマージします。

issue や PR を立てる場合は、私のような初心者にも優しくしてくれるとうれしいです。  
特にテンプレとかは書かないですし、**大半の人がみて分かりやすいような書き方**であれば何でもいいです。  
なお、Contribute用のガイドは[こちら](https://github.com/team-i2021/nira_bot/blob/release/CONTRIBUTING.md)にあります。

# 機能

[こちら](https://nira.f5.si/help.html)をご確認ください。

# Extra Licenses

- Words list for Wordle  
  『CEFR-J Wordlist Version 1.6』 東京外国語大学投野由紀夫研究室. （URL: http://www.cefr-j.org/download.html より 2022 年 02 月ダウンロード）

- TTS Character Voice
  TTS の読み上げ音声には、VOICEVOX Web API を使用しています。  
  [VOICEVOX Web API (高速)](https://voicevox.su-shiki.com/su-shikiapis/)  
  [キャラクターボイス: `VOCEVOX`](https://voicevox.hiroshiba.jp/)  
  **公序良俗に反する読み上げは一部のキャラクターでは、利用規約違反となります。**

# 最後に

優しく見守ってくださいませ
