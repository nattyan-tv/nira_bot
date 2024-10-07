# にらBOT CONTRIBUTING

## はじめに

他のコードを1度は見てから書くことを推奨します。  
命名規則やコードの規則について、明確な規則はなく**完全な**順守はしてはいません。  
ですが、なるべく他のコードと似たような形で、汚くなりすぎないよう心がけてください。

また、そのコードが動くことを検証してください。  
検証が不可能な場合は、その旨を明記していただければ大丈夫です。

## Issue

現行開発者以外の方のIssueは、バグ修正などをメインに受け付けます。  
また、その際はプログラムに対しての理解がある程度あり、どこのコードが問題であるかなどが明確になっていることが望ましいです。  
そうでない場合は、Discordサーバーの`#enhance-fix`で相談していただければと思います。

出来る限りタグをつけていただければ嬉しいです。

## Pull Request

Pull Requestは、`develop`ブランチに対して送っていただければ、レビューを行った上でマージします。

PRを送る際は、出来る限り最初にDraftを立ててください。  
タイトルや説明文には、そのPRが何をするものなのか、どのような変更を行ったのかを（他のPRなどを参考にしながら）明記してください。

また、レビューリクエストやメンションなどは遠慮なく行って頂きたいのですが、動作を検証したうえでリクエスト頂ければ嬉しいです。


### NIRAオブジェクトについて

以下は使い物にならないドキュメントです...


`util/nira.py`にあるNIRAオブジェクトは、`commands.Bot`を継承したクラスです。  
基本的に`commands.Bot`と同じ動作をします。  
ですが、一部関数やメソッドにおいて異なる動作をします。

### Method
- `NIRA.debug`  
    type: `bool`  
    description: BOTのデバッグモード(`-d`オプションによる起動)が有効かどうかを示します。

- `NIRA.__token`  
    type: `str`  
    description: BOTの起動に使用されるトークンです。  
    デバッグ環境で誤って`bot.token`と入力してもトークンが流出しないように、あえて名前を変えています。  
    今になって効果があるかどうかはまったくもって不明です。

- `NIRA.database`  
    type: `motor.motor_asyncio.AsyncIOMotorDatabase`  
    description: MongoDBのデータベースです。

### Function
- `NIRA.run`  
    args: ()  
    return: None  
    description: BOTを起動します。トークンは、`token`で指定されたものを使用します。

- `NIRA.is_owner`  
    args: (user: discord.User)  
    return: bool  
    description: 指定されたユーザーがBOTの管理者かどうか（py_adminに含まれるか、BOTの所有者か）を示します。
