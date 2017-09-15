import asyncio
from discord.ext import commands

import sys

class OwnerTools():
    def __init__(self, bot):
        self.bot = bot
        self.fixed = [ "owner_tools" ]

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send("Cerrando sesion...")
        await self.bot.logout()
        sys.exit(0)

    @commands.command()
    @commands.is_owner()
    async def guilds(self, ctx):
        glist = "Lista de Guilds/Servidores usando al Bot:\n\n"
        for g in self.bot.guilds:
            glist += "**{}** / *{}*\n".format(g.name, g.id)
        glist += "\nTotal: **{}**".format(len(self.bot.guilds))
        await ctx.send(glist)

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, ext):
        self.bot.load_extension("addons." + ext)
        await ctx.send("El addon **{}** ha sido activado.".format(ext))

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, ext):
        if ext in self.fixed:
            await ctx.send("Este addon no puede ser desactivado.")
            return
        self.bot.unload_extension(ext)
        await ctx.send("El addon **{}** ha sido desactivado.".format(ext))

def setup(bot):
    bot.add_cog(OwnerTools(bot))
