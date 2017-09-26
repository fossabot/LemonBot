import asyncio,logging
from discord.ext import commands

class ErrorHandler():
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, ctx, error):
        await ctx.send("Ha ocurrido un error:\n```{}: {}\n```".format(type(error), error))

def setup(bot):
    bot.add_cog(ErrorHandler(bot))
