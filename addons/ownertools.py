import asyncio,logging
from discord.ext import commands

class OwnerTools():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send("Bye bye!")
        await self.bot.logout()

    @commands.command()
    @commands.is_owner()
    async def guilds(self, ctx):
        txt = "Lista de Guilds:\n\n"
        for g in self.bot.guilds:
            txt += "*{}* / **{}**\n".format(g.name, g.id)
        await ctx.send(txt)

def setup(bot):
    bot.add_cog(OwnerTools(bot))
