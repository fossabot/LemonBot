import asyncio,logging
from dataIOpy import js
from discord.ext import commands

class Info():
    def __init__(self, bot):
        self.bot = bot
        self.config = js.load("config/info.json")

    @commands.command()
    async def info(self, ctx):
        await ctx.send(self.config["info_text"])
        
    @commands.command()
    async def help(self, ctx):
        await ctx.send(self.config["help_text"])
        
def setup(bot):
    bot.add_cog(Info(bot))
