# coding: utf-8
from math import e
from re import M
import discord
import asyncio
from util import n_fc

async def n_help(message, client):
    if message.content == "n!help":
        cn = "help"
    else:
        cn = message.content[7:]
    embed = discord.Embed(title="にらBOT HELP", description=f"```n!{cn}```", color=0x00ff00)
    embed.set_author(name="製作者：なつ", url="https://twitter.com/nattyan_tv", icon_url="https://pbs.twimg.com/profile_images/1388437778292113411/pBiEOtHL_400x400.jpg")
    if cn == "ss":
        embed.add_field(name="```ss```", value="Steam個人サーバーの状況をチェックします。\n`n!ss`以外は管理者権限が必要です。", inline=False)
        embed.add_field(name="```n!ss add [サーバー名] [アドレス],[ポート番号]```", value="サーバーのリストに追加します。", inline=False)
        embed.add_field(name="`[サーバー名]`", value="サーバーに付ける名前を入力します。", inline=False)
        embed.add_field(name="`[アドレス]`", value="サーバーのアドレスを追加します。（グローバルIPアドレス）", inline=False)
        embed.add_field(name="`[ポート番号]`", value="サーバーのポートを追加します。", inline=False)
        embed.add_field(name="例", value="```n!ss add マップ1のさば 0.0.0.0,80```", inline=False)
        embed.add_field(name="```n!ss edit [サーバーナンバー] [サーバー名] [アドレス],[ポート番号]```", value="サーバーのリストを編集します。", inline=False)
        embed.add_field(name="`[サーバーナンバー]`", value="`n!ss list`などで、サーバーナンバー（*_adや*_nmの「*」の部分）を確認してください。", inline=False)
        embed.add_field(name="`[サーバー名]`", value="サーバーに付ける名前を入力します。", inline=False)
        embed.add_field(name="`[アドレス]`", value="サーバーのアドレスを追加します。（グローバルIPアドレス）", inline=False)
        embed.add_field(name="`[ポート番号]`", value="サーバーのポートを追加します。", inline=False)
        embed.add_field(name="例", value="```n!ss edit 1 マップ1の味噌鯖 0.0.0.0,8080```", inline=False)
        embed.add_field(name="```n!ss list```", value="サーバーのリストを表示します。", inline=False)
        embed.add_field(name="例", value="```n!ss list```", inline=False)
        embed.add_field(name="```n!ss del [サーバーナンバー]```", value="リストから一つ選択してサーバーを削除します。", inline=False)
        embed.add_field(name="例", value="```n!ss del 1```", inline=False)
        embed.add_field(name="```n!ss del all```", value="サーバーのリストを全て削除します。", inline=False)
        embed.add_field(name="例", value="```n!ss del all```", inline=False)
        embed.add_field(name="```n!ss auto [on/off]```", value="30分ごとにサーバーステータスを取得して、鯖落ちしてたらメンションします。", inline=False)
        embed.add_field(name="```[on/off]```", value="onにすると30分ごとにサーバーステータスを取得します。offにするか、鯖落ちが発生するまでずっと実行されます。\nここの値を指定しないと、AutoSSの状態を表示します。", inline=False)
        embed.add_field(name="例", value="```n!ss auto on```", inline=False)
    elif cn == "embed":
        embed.add_field(name="```embed```", value="Embedを作成して送信します。", inline=False)
        embed.add_field(name="```n!embed [カラー] [タイトル]\n[本文]```", value="サーバーのリストに追加します。", inline=False)
        embed.add_field(name="`[カラー]`", value="サーバーに付ける名前を入力します。", inline=False)
        embed.add_field(name="`[タイトル]`", value="サーバーのアドレスを追加します。（グローバルIPアドレス）", inline=False)
        embed.add_field(name="`[本文]`", value="サーバーのポートを追加します。", inline=False)
        embed.add_field(name="例", value="```n!embed 00ff00 これはにら。\nにらってうまいよなぁ...\nレバニラとかおいしいよな...```", inline=False)
    elif cn == "srtr":
        embed.add_field(name="```srtr```", value="しりとり（風の対話）を始めます。", inline=False)
        embed.add_field(name="```n!srtr start```", value="そのチャンネルでしりとり（風の対話）を始めます。", inline=False)
        embed.add_field(name="例", value="```n!srtr start```\n", inline=False)
        embed.add_field(name="```n!srtr stop```", value="そのチャンネルでのしりとりを終了します。", inline=False)
        embed.add_field(name="例", value="```n!srtr stop```", inline=False)
    elif cn == "janken":
        embed.add_field(name="```janken```", value="じゃんけんで遊びます。確率操作はしてません。", inline=False)
        embed.add_field(name="```n!janken [出す手]```", value="じゃんけんできます。それだけです。", inline=False)
        embed.add_field(name="`[出す手]`", value="グーかチョキかパーでお願いしますっ", inline=False)
        embed.add_field(name="例", value="```n!janken グー```", inline=False)
    elif cn == "uranai":
        embed.add_field(name="```uranai```", value="あなたの運勢が占われます。確率ｓ(ry", inline=False)
        embed.add_field(name="```n!uranai```", value="にらが占ってあげましょう...", inline=False)
        embed.add_field(name="例", value="```n!uranai```", inline=False)
    elif cn == "nr":
        embed.add_field(name="```nr```", value="サーバーおよびチャンネルごとに通常反応の設定を変更します。\n確認以外は管理者権限が必要です。", inline=False)
        embed.add_field(name="```n!nr```", value="チャンネルの通常反応設定の確認を行います。（サーバーで無効になっている場合はそちらが表示されます。）", inline=False)
        embed.add_field(name="例", value="```n!nr```\n", inline=False)
        embed.add_field(name="```n!nr [コマンド]```", value="チャンネルごとに通常反応設定変更を行います。", inline=False)
        embed.add_field(name="`[コマンド]`", value="Trueで通常反応有効、Falseで通常反応が無効になります。", inline=False)
        embed.add_field(name="例", value="```n!nr true```", inline=False)
        embed.add_field(name="```n!nr all [コマンド]```", value="サーバーでの通常反応設定変更を行います。", inline=False)
        embed.add_field(name="`[コマンド]`", value="Trueで通常反応有効、Falseで通常反応が無効になります。\nサーバーで通常反応設定が無効になっている場合は、チャンネルごとの設定も無効になります。", inline=False)
        embed.add_field(name="例", value="```n!nr all false```", inline=False)
    elif cn == "er":
        embed.add_field(name="```er```", value="追加反応を設定します。\n`n!er list`以外は管理者権限が必要です。", inline=False)
        embed.add_field(name="```n!er add [トリガー] [リターン]```", value="追加反応のリストに追加します。", inline=False)
        embed.add_field(name="`[トリガー]`", value="反応する文を入力します。", inline=False)
        embed.add_field(name="`[リターン]`", value="返信する文を入力します。", inline=False)
        embed.add_field(name="例", value="```n!er add くろねこ かっこいい```", inline=False)
        embed.add_field(name="```n!er edit [トリガー] [リターン]```", value="追加反応のリストを編集します。", inline=False)
        embed.add_field(name="`[トリガー]`", value="反応する文を入力します。", inline=False)
        embed.add_field(name="`[リターン]`", value="返信する文を入力します。", inline=False)
        embed.add_field(name="例", value="```n!ss edit くろねこ クール！```", inline=False)
        embed.add_field(name="```n!er list```", value="追加反応のリストを表示します。", inline=False)
        embed.add_field(name="例", value="```n!er list```", inline=False)
        embed.add_field(name="```n!er del```", value="追加反応のリストを削除します。", inline=False)
        embed.add_field(name="例", value="```n!er del```", inline=False)
    elif cn == "nr":
        embed.add_field(name="```ui```", value="サーバーにユーザーが入ってきたときにそのユーザーの情報を表示するようにします。\n管理者権限が必要です。", inline=False)
        embed.add_field(name="```n!ui set [チャンネルID]```", value="ユーザーの情報を表示させるようにします。", inline=False)
        embed.add_field(name="`[チャンネルID]`", value="表示させるチャンネルのIDを入力します。", inline=False)
        embed.add_field(name="例", value="```n!ui 123456789```\n", inline=False)
        embed.add_field(name="```n!ui del```", value="ユーザーの情報を表示させないようにします。", inline=False)
        embed.add_field(name="例", value="```n!nr del```", inline=False)
        embed.add_field(name="```n!ui```", value="ユーザーの情報を表示させるように設定しているチャンネルの名前を表示します。", inline=False)
        embed.add_field(name="例", value="```n!nr```", inline=False)
    elif cn == "d":
        embed.add_field(name="```d```", value="指定したユーザーの情報を表示します。", inline=False)
        embed.add_field(name="```n!d [ユーザーID]```", value="指定したユーザーの情報を表示します。", inline=False)
        embed.add_field(name="`[ユーザーID]`", value="表示するユーザーを指定します。", inline=False)
        embed.add_field(name="例", value="```n!d 892759276152573953```\n", inline=False)
        embed.add_field(name="```n!d```", value="自分自身の情報を表示します。", inline=False)
        embed.add_field(name="例", value="```n!d```", inline=False)
    else:
        embed = discord.Embed(title="にらBOT HELP（にらちゃんの使い方）", description="気になるコマンドがあったら`n!help [command]`で調べてみよう！", color=0x00ff00)
        embed.set_author(name="製作者：なつ", url="https://twitter.com/nattyan_tv", icon_url="https://pbs.twimg.com/profile_images/1388437778292113411/pBiEOtHL_400x400.jpg")
        embed.add_field(name="```help```", value="このヘルプを表示します。", inline=False)
        embed.add_field(name="```ss```", value="Steam個人サーバーの状況をチェックします。", inline=False)
        embed.add_field(name="```embed```", value="Embedを作成して送信します。", inline=False)
        embed.add_field(name="```srtr```", value="しりとり（風の対話）を始めます。", inline=False)
        embed.add_field(name="```janken```", value="じゃんけんで遊びます。確率操作はしてません。", inline=False)
        embed.add_field(name="```uranai```", value="あなたの運勢が占われます。確率ｓ(ry", inline=False)
        embed.add_field(name="```nr```", value="通常反応の設定を変更します。", inline=False)
        embed.add_field(name="```er```", value="追加返事機能の設定を行います。", inline=False)
        embed.add_field(name="```ui```", value="サーバーにユーザーが入ってきたときにそのユーザーの情報を表示するようにします。", inline=False)
        embed.add_field(name="```d```", value="指定されたユーザーの情報を表示します。", inline=False)
        embed.add_field(name="・リアクションについて", value="このbotの発したメッセージの一部には、<:trash:908565976407236608>のリアクションが自動的に付きます。\nこのリアクションを押すとそのメッセージが削除されます。", inline=False)
    await message.reply(embed=embed)