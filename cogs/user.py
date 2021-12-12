from discord.ext import commands
import discord
import re
import pickle

import sys

from discord.ext.commands.core import command
sys.path.append('../')
from util import admin_check, n_fc, eh

#ユーザー情報表示系

class user(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def d(self, ctx: commands.Context):
        if ctx.message.content == "n!d":
            user = await self.bot.fetch_user(ctx.message.author.id)
            embed = discord.Embed(title="User Info", description=f"名前：`{user.name}`\nID：`{user.id}`", color=0x00ff00)
            embed.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user.id}/{str(user.avatar)}")
            embed.add_field(name="アカウント製作日", value=f"```{user.created_at}```")
            await ctx.message.reply(embed=embed)
            return
        else:
            user_id = int("".join(re.findall(r'[0-9]', ctx.message.content[4:])))
            try:
                user = await self.bot.fetch_user(user_id)
                embed = discord.Embed(title="User Info", description=f"名前：`{user.name}`\nID：`{user.id}`", color=0x00ff00)
                embed.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user.id}/{str(user.avatar)}")
                embed.add_field(name="アカウント製作日", value=f"```{user.created_at}```")
                await ctx.message.reply(embed=embed)
                return
            except BaseException:
                await ctx.message.reply(embed=discord.Embed(title="Error", description="ユーザーが存在しないか、データが取得できませんでした。", color=0xff0000))
                return
    
    @commands.command()
    async def ui(self, ctx: commands.Context):
        if admin_check.admin_check(ctx.message.guild, ctx.message.author) or ctx.message.author.id in n_fc.py_admin:
            if ctx.message.content[:8] == "n!ui set":
                try:
                    set_id = int("".join(re.findall(r'[0-9]', ctx.message.content[9:])))
                    n_fc.welcome_id_list[ctx.message.guild.id] = set_id
                    with open('/home/nattyantv/nira_bot_rewrite/welcome_id_list.nira', 'wb') as f:
                        pickle.dump(n_fc.welcome_id_list, f)
                    channel = self.bot.get_channel(n_fc.welcome_id_list[ctx.message.guild.id])
                    await channel.send("追加完了メッセージ\nこのメッセージが指定のチャンネルに送信されていれば完了です。")
                    await ctx.message.reply("追加完了のメッセージを指定されたチャンネルに送信しました。\n送信されていない場合はにらBOTに適切な権限が与えられているかご確認ください。")
                    return
                except BaseException as err:
                    await ctx.message.reply(embed=eh.eh(err))
                    return
            elif ctx.message.content == "n!ui del":
                try:
                    if ctx.message.guild.id not in n_fc.reaction_bool_list:
                        seted_id = n_fc.welcome_id_list[ctx.message.guild.id]
                        del n_fc.welcome_id_list[ctx.message.guild.id]
                        with open('/home/nattyantv/nira_bot_rewrite/welcome_id_list.nira', 'wb') as f:
                            pickle.dump(n_fc.welcome_id_list, f)
                        await ctx.message.reply(f"削除しました。\n再度同じ設定をする場合は```n!ui set {seted_id}```と送信してください。")
                        return
                    else:
                        await ctx.message.reply("設定されていません。")
                        return
                except BaseException as err:
                    await ctx.message.reply(embed=eh.eh(err))
                    return
            elif ctx.message.content == "n!ui":
                try:
                    if ctx.message.guild.id in n_fc.reaction_bool_list:
                        seted_id = int(n_fc.welcome_id_list[ctx.message.guild.id])
                        channel = self.bot.get_channel(int(n_fc.welcome_id_list[ctx.message.guild.id]))
                        await ctx.message.reply(f"チャンネル：{channel.name}")
                        return
                    else:
                        await ctx.message.reply("設定されていません。\n\n・追加```n!ui set [チャンネルID]```・削除```n!ui del```")
                        return
                except BaseException as err:
                    await ctx.message.reply(embed=eh.eh(err))
                    return
        else:
            await ctx.message.reply(embed=discord.Embed(title="Error", description=f"管理者権限がありません。", color=0xff0000))
            return

def setup(bot):
    bot.add_cog(user(bot))