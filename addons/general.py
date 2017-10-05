from discord.ext import commands
import sys
import discord

class Info():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["help", "about"])
    async def info(self, ctx):
        embed = discord.Embed(
            title=self.bot.loc("general_title").format(self.bot.name),
            description=self.bot.loc("general_description").format(
                c=self.bot.help, r=self.bot.repo
            ),
            url=self.bot.web,
            colour=0xe95420
        )
        embed.add_field(name=self.bot.loc("general_version_bot"),
                        value=self.bot.version)
        embed.add_field(name=self.bot.loc("general_version_py"),
                        value=sys.version.split()[0])
        embed.add_field(name=self.bot.loc("general_version_dpy"),
                        value=discord.__version__)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))
