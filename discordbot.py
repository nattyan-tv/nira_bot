import discord
from os import getenv

import re
import random

line_url = 'https://notify-api.line.me/api/notify'

TOKEN = getenv('DISCORD_BOT_TOKEN')

client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    print('正常に起動しました')
    print('でぃすこたん v0.9.2')
    print('～故に彼女は猫だった～')
    await client.change_presence(activity=discord.Game(name="にゃんこのでぃすこたん", type=1))

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    global memo
    memo = ""
    # 下のやつミスると「v0.9.2　～故に彼は猫だった～」の時みたいに猫爆弾が起爆するにゃ(botのメッセージは無視する)
    if message.author.bot:
        return
    # 猫系のワードに反応するにゃ
    if re.search(r'(?:nyanko|neko|cat|cats|猫|ねこ|ネコ|にゃんこ|ニャンコ|NYANKO|NEKO|CAT|CATS|にゃん|にゃー|にゃ～)', message.content):
        neko_rnd = random.randint(1, 3)
        if neko_rnd == 1:
            await message.channel.send('にゃ、にゃーん？')
        elif neko_rnd == 2:
            await message.channel.send('ねこだにゃーん？')
        elif neko_rnd == 3:
            await message.channel.send('ごろにゃーん！')
        return
    if re.search(r'(?:めも |メモ |memo )', message.content):
        mes_cnt = message.content
        memo = mes_cnt.split(" ", 2)[1]
        await message.channel.send('記録しました')
        return
    if re.search(r'(?:めも　|メモ　|memo　)', message.content):
        mes_cnt = message.content
        memo = mes_cnt.split("　", 2)[1]
        await message.channel.send('記録しました')
        return
    if message.content == "メモ" or message.content == "めも" or message.content == "memo":
        await message.channel.send(memo)
        return
    return


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
