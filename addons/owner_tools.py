import config,asyncio,localize
from discord.ext import commands
import sys

class OwnerTools():
    def __init__(self, bot):
        self.bot = bot
        self.strings = localize.LocalizeMe("strings", config.lang)
        self.fixed = [ "owner_tools" ]

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send(self.strings.get("ot_logging_out"))
        self.bot.logout()
        sys.exit(0)

    @commands.command()
    @commands.is_owner()
    async def guilds(self, ctx):
        glist = self.strings.get("ot_guild_list")
        for g in self.bot.guilds:
            glist += "**{}** / *{}*\n".format(g.name, g.id)
        glist += "\nTotal: **{}**".format(len(self.bot.guilds))
        await ctx.send(glist)

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, ext):
        self.bot.load_extension("addons." + ext)
        await ctx.send(self.strings.get("ot_addon_enabled").format(addon=ext))

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, ext):
        if ext in self.fixed:
            await ctx.send(self.strings.get("ot_addon_fixed").format(addon=ext))
            return
        self.bot.unload_extension(ext)
        await ctx.send(self.strings.get("ot_addon_disabled").format(addon=ext))

def setup(bot):
    bot.add_cog(OwnerTools(bot))
