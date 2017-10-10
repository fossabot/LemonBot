from discord.ext import commands

class OwnerTools():
    def __init__(self, bot):
        self.bot = bot
        self.fixed = ["general", "owner_tools"]

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send(self.bot.loc("ot_logging_out"))
        await self.bot.logout()

    @commands.command()
    @commands.is_owner()
    async def guilds(self, ctx):
        glist = self.bot.loc("ot_guild_list")
        for guild in self.bot.guilds:
            glist += "**{}** / *{}*\n".format(guild.name, guild.id)
        glist += "\nTotal: **{}**".format(len(self.bot.guilds))
        await ctx.send(glist)

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, ext : str):
        try:
            self.bot.load_extension("addons." + ext)
        except ImportError:
            await ctx.send(self.bot.loc("ot_addon_loaderror").format(ext))
        else:
            await ctx.send(self.bot.loc("ot_addon_enabled").format(ext))

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, ext : str):
        if ext in self.fixed:
            await ctx.send(self.bot.loc("ot_addon_fixed").format(ext))
            return
        self.bot.unload_extension("addons." + ext)
        await ctx.send(self.bot.loc("ot_addon_disabled").format(ext))

def setup(bot):
    bot.add_cog(OwnerTools(bot))
