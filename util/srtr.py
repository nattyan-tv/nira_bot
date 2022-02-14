# coding: utf-8
import nextcord
from os import getenv
import re
import random
import jaconv
import util.word_data as word_data
import pykakasi

re_hiragana = re.compile(r'^[あ-ん]+$')
re_katakana = re.compile(r'[\u30A1-\u30F4]+')
re_alpha = re.compile(r'^[a-zA-Z]+$')
re_kanji = re.compile(r'^[\u4E00-\u9FD0]+$')


kks = pykakasi.kakasi()

async def on_srtr(message):
    global ply_dt
    ply_dt = []
    if message.author.bot:
        return
    if not re_alpha.fullmatch(message.content):
        srtr_str = kks.convert(message.content)
    else:
        srtr_str = message.content
    if not re.sub("[^0-9A-Za-z\u3041-\u3096\u30A1-\u30FA\u4E00-\u9FFF\uF900-\uFA6D\uFF66-\uFF9D]+", "", srtr_str) == "":
        last_str = re.sub("[^0-9A-Za-z\u3041-\u3096\u30A1-\u30FA\u4E00-\u9FFF\uF900-\uFA6D\uFF66-\uFF9D]+", "", srtr_str)[-1]
    else:
        return
    if re_katakana.fullmatch(last_str):
        lstr = jaconv.kata2hira(last_str)
    elif re_hiragana.fullmatch(last_str):
        lstr = last_str
    elif re_alpha.fullmatch(last_str):
        lstr = last_str.lower()
    else:
        return
    if lstr in word_data.chara_ary:
        w_rn = []
        while True:
            exec("ply_dt = word_data." + lstr + "_wd", globals())
            rnd = random.randint(1, len(ply_dt))
            rnd = rnd - 1
            if rnd not in w_rn:
                reply_mes = ply_dt[rnd]
                await message.reply(reply_mes)
                break
            else:
                continue
    else:
        return

