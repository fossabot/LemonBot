import config
from addons.tools.localize import LocalizeMe
from discord.ext import commands

class Info():
    def __init__(self, bot):
        self.bot = bot
        self.strings = LocalizeMe("strings", config.lang)

    @commands.command()
    async def info(self, ctx):
        await ctx.send(self.strings.get("general_info"))
        
    @commands.command()
    async def help(self, ctx):
        await ctx.send(self.strings.get("general_commands"))
        
def setup(bot):
    bot.add_cog(Info(bot))
