import config
from addons.tools.localize import LocalizeMe
from discord.ext import commands

import sys
import bot
import discord

class Info():
    def __init__(self, bot):
        self.bot = bot
        self.strings = LocalizeMe("strings", config.lang)

    @commands.command(aliases=["help", "about"])
    async def info(self, ctx):
        embed = discord.Embed(
            title=self.strings.get("general_title").format(bot.name),
            description=self.strings.get("general_description").format(c=bot.bhelp, r=bot.repo),
            url=bot.webpage,
            colour=0xe95420
        )
        embed.add_field(name=self.strings.get("general_botversion"), value=bot.version)
        embed.add_field(name=self.strings.get("general_pyversion"), value=sys.version.split()[0])
        embed.add_field(name=self.strings.get("general_dpyversion"), value=discord.__version__)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))
