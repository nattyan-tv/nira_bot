import asyncio
import logging
import math
import random
import time
from re import compile

import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands, tasks, application_checks

from motor import motor_asyncio

from util.n_fc import on_ali, off_ali
from util.nira import NIRA

SET, DEL, STATUS = (0, 1, 2)
ROLE_ID = compile(r"<@&[\d]+?>")

class UpNotify(commands.Cog):
    def __init__(self, bot: NIRA):
        self.bot = bot
        self.collection: motor_asyncio.AsyncIOMotorCollection = self.bot.database["up_notify"]

    @commands.guild_only()
    @commands.has_permissions(manage_guild=True)
    @commands.command(name="up", aliases=["アップ", "あっぷ", "dissoku"], help="""\
DissokuのUp通知を行います

もうそのまんまです。
DissokuのUpをしたら、その1時間後に通知します。


・使い方
`n!up [on/off] [*ロール]`
**on**の場合、ロールを後ろにつけると、通知時にロールをメンションします。

・例
`n!up on`
`n!up on @( ᐛ )وｱｯﾊﾟｧｧｧｧｧｧｧｧｧｧｧｧｧｧ!!`
`n!up off`""")
    async def up(self, ctx: commands.Context, option: str | None = None, role_str: str | None = None):
        assert ctx.guild
        upper = await self.collection.find_one({"guild_id": ctx.guild.id})
        if option is None:
            if upper is None:
                await ctx.reply(embed=nextcord.Embed(
                    title="Up通知",
                    description=f"この`{ctx.guild.name}`にはUp通知が設定されていません。",
                    color=0x00ff00
                ))
            else:
                if upper["role_id"] is None:
                    await ctx.reply(embed=nextcord.Embed(
                        title="Up通知",
                        description=f"この`{ctx.guild.name}`にはUp通知が設定されています。\nメンションロール: なし",
                        color=0x00ff00
                    ))
                else:
                    await ctx.reply(embed=nextcord.Embed(
                        title="Up通知",
                        description=f"この`{ctx.guild.name}`にはUp通知が設定されています。\nメンションロール: <@&{upper['role_id']}>",
                        color=0x00ff00
                    ))
        elif option in on_ali:
            if role_str is None:
                await self.collection.update_one({"guild_id": ctx.guild.id}, {"$set": {"role_id": None}}, upsert=True)
                await ctx.reply(embed=nextcord.Embed(
                    title="Up通知",
                    description=f"この`{ctx.guild.name}`でUp通知が設定されました。\nメンションロール: なし",
                    color=0xff0000
                ))
                return
            if role := ROLE_ID.fullmatch(role_str):
                if upper is None:
                    upper = {"guild_id": ctx.guild.id, "role_id": int(role.group().replace("<@&", "").replace(">", ""))}
                else:
                    upper["role_id"] = int(role.group().replace("<@&", "").replace(">", ""))

                await self.collection.update_one({"guild_id": ctx.guild.id}, {"$set": upper}, upsert=True)

                await ctx.reply(embed=nextcord.Embed(
                    title="Up通知",
                    description=f"この`{ctx.guild.name}`にはUp通知が設定されています。\nメンションロール: <@&{upper['role_id']}>",
                    color=0x00ff00
                ))
            else:
                try:
                    role = ctx.guild.get_role(int(role_str))
                except ValueError:
                    pass

                if role is None:
                    for i in ctx.guild.roles:
                        if i.name == role_str:
                            role = i
                            break

                if role is None:
                    await ctx.reply(embed=nextcord.Embed(title="エラー", description=f"指定したロール`{role_str}`が見つかりませんでした。", color=0xff0000))
                    return

                await self.collection.update_one({"guild_id": ctx.guild.id}, {"$set": {"role_id": role.id}}, upsert=True)
                await ctx.reply(embed=nextcord.Embed(
                    title="Up通知",
                    description=f"この`{ctx.guild.name}`でUp通知が設定されました。\nメンションロール: <@&{role.id}>",
                    color=0x00ff00
                ))
        elif option in off_ali:
            if upper is None:
                await ctx.reply(embed=nextcord.Embed(
                    title="Up通知",
                    description=f"この`{ctx.guild.name}`にはUp通知が設定されていません。",
                    color=0xff0000
                ))
            else:
                await self.collection.delete_one({"guild_id": ctx.guild.id})
                await ctx.reply(embed=nextcord.Embed(
                    title="Up通知",
                    description=f"この`{ctx.guild.name}`でのUp通知設定を解除しました。",
                    color=0x00ff00
                ))
        else:
            await ctx.reply(embed=nextcord.Embed(
                title="エラー",
                description="指定したオプションが不正です。\n`n!up [on/off] [*ロール]`",
                color=0xff0000
            ))


    @application_checks.guild_only()
    @application_checks.has_permissions(manage_guild=True)
    @nextcord.slash_command(name="up", description="Dissoku notification")
    async def up_slash(self, interaction: Interaction):
        pass


    @application_checks.guild_only()
    @application_checks.has_permissions(manage_guild=True)
    @up_slash.subcommand(name="on", description="Turn ON notification of Dissoku", description_localizations={nextcord.Locale.ja: "Dissoku通知を有効にします"})
    async def up_slash_on(
        self,
        interaction: Interaction,
        role: nextcord.Role | None = SlashOption(
            name="role",
            description="Role of mention",
            description_localizations={nextcord.Locale.ja: "メンションするロールです"},
            required=False
        )
    ):
        await interaction.response.defer(ephemeral=True)
        assert interaction.guild

        if role is None:
            await self.collection.update_one({"guild_id": interaction.guild.id}, {"$set": {"role_id": None}}, upsert=True)
            mention_role = "なし"
        else:
            await self.collection.update_one({"guild_id": interaction.guild.id}, {"$set": {"role_id": role.id}}, upsert=True)
            mention_role = f"<@&{role.id}>"

        await interaction.send(embed=nextcord.Embed(
            title="Up通知",
            description=f"この`{interaction.guild.name}`にはUp通知が設定されています。\nメンションロール: {mention_role}",
            color=0x00ff00
        ))


    @application_checks.guild_only()
    @application_checks.has_permissions(manage_guild=True)
    @up_slash.subcommand(name="off", description="Turn OFF notification of Dissoku", description_localizations={nextcord.Locale.ja: "Dissoku通知を無効にします"})
    async def up_slash_off(self, interaction: Interaction):
        await interaction.response.defer(ephemeral=True)
        assert interaction.guild
        upper = await self.collection.find_one({"guild_id": interaction.guild.id})

        if upper is None:
            await interaction.send(embed=nextcord.Embed(
                title="Up通知",
                description=f"この`{interaction.guild.name}`にはUp通知が設定されていません。",
                color=0xff0000
            ))
        else:
            await self.collection.delete_one({"guild_id": interaction.guild.id})
            await interaction.send(embed=nextcord.Embed(
                title="Up通知",
                description=f"この`{interaction.guild.name}`でのUp通知設定を解除しました。",
                color=0x00ff00
            ))


    @application_checks.guild_only()
    @application_checks.has_permissions(manage_guild=True)
    @up_slash.subcommand(name="status", description="Status of notification of Dissoku", description_localizations={nextcord.Locale.ja: "Dissoku通知の状態を確認します"})
    async def up_slash_status(self, interaction: Interaction):
        await interaction.response.defer(ephemeral=True)
        assert interaction.guild
        upper = await self.collection.find_one({"guild_id": interaction.guild.id})

        if upper is None:
            await interaction.send(embed=nextcord.Embed(
                title="Up通知",
                description=f"この`{interaction.guild.name}`にはUp通知が設定されていません。",
                color=0x00ff00
            ))
        else:
            if upper["role_id"] is None:
                await interaction.send(embed=nextcord.Embed(
                    title="Up通知",
                    description=f"この`{interaction.guild.name}`にはUp通知が設定されています。\nメンションロール: なし",
                    color=0x00ff00
                ))
            else:
                await interaction.send(embed=nextcord.Embed(
                    title="Up通知",
                    description=f"この`{interaction.guild.name}`にはUp通知が設定されています。\nメンションロール: <@&{upper['role_id']}>",
                    color=0x00ff00
                ))


    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if isinstance(message.channel, nextcord.DMChannel):
            return
        if message.guild is None:
            return
        result = await self.collection.find_one({"guild_id": message.guild.id})
        if result is None:
            return
        if message.author.id != 761562078095867916:
            return
        for _ in range(20):
            # ディス速通知はメッセージが後からeditされるので、それを待つために何回か繰り返す
            message = await message.channel.fetch_message(message.id)
            assert message.guild
            if message.embeds == []:
                await asyncio.sleep(1)
                continue
            if message.embeds[0].title != "ディスコード速報 | Discordサーバー・友達募集・ボット掲示板":
                await asyncio.sleep(1)
                continue
            if message.embeds[0].fields[0].name == f"`{message.guild.name}` をアップしたよ!":
                try:
                    logging.info(f"Up通知 {message.guild.id} をセット")
                    await message.channel.send(embed=nextcord.Embed(title="Up通知設定", description=f"<t:{math.floor(time.time())+3600}:f>、<t:{math.floor(time.time())+3600}:R>に通知します。", color=0x00ff00))
                    await asyncio.sleep(3600)
                    up_rnd = random.randint(1, 3)
                    messageContent = ""
                    if result["role_id"] is None:
                        messageContent = "にらBOT Up通知"
                    else:
                        messageContent = f"<@&{result['role_id']}>"
                    if up_rnd == 1:
                        await message.channel.send(messageContent, embed=nextcord.Embed(title="Upの時間だけどぉ！？！？", description=f"ほらほら～Upしないのぉ？？？\n```/dissoku up```", color=0x00ff00))
                    elif up_rnd == 2:
                        await message.channel.send(messageContent, embed=nextcord.Embed(title="Upしやがれください！", description=f"お前がUpするんだよ、あくしろよ！\n```/dissoku up```", color=0x00ff00))
                    elif up_rnd == 3:
                        await message.channel.send(messageContent, embed=nextcord.Embed(title="Upしましょう！", description=f"Upしてみませんか！\n```/dissoku up```", color=0x00ff00))
                    return
                except Exception as err:
                    logging.error(err)
                    return
            else:
                return


def setup(bot: NIRA):
    bot.add_cog(UpNotify(bot))
