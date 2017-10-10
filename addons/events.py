from discord.ext import commands

class Events:
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, ctx, error):
        if self.bot.dev:
            await ctx.send(self.bot.loc("events_error_development").format(
                t=type(error), e=error))
        else:
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send(self.bot.loc("events_error_pmissing").format(error.param))
            elif isinstance(error, commands.NoPrivateMessage):
                await ctx.send(self.bot.loc("events_error_pmdisabled"))
            elif isinstance(error, commands.CommandOnCooldown):
                await ctx.send(self.bot.loc("events_error_cooldown").format(error.retry_after))
            elif isinstance(error, commands.NotOwner):
                await ctx.send(self.bot.loc("events_error_owneronly"))
            elif isinstance(error, commands.MissingPermissions):
                await ctx.send(self.bot.loc("events_error_u_cant"))
            elif isinstance(error, commands.BotMissingPermissions):
                await ctx.send(self.bot.loc("events_error_b_cant"))
            else:
                await ctx.send(self.bot.loc("events_error_generic"))

def setup(bot):
    bot.add_cog(Events(bot))
