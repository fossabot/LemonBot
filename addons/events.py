from discord.ext import commands
import discord

class Events():
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print(self.bot.loc("events_ready").format(
            un=self.bot.user, id=self.bot.user.id,
            gc=len(self.bot.guilds), gu=len(self.bot.users)))
        game = discord.Game(name=self.bot.loc("events_playing").format(
            v=self.bot.version, g=len(self.bot.guilds), p=self.bot.prefix))
        await self.bot.change_presence(game=game)

    async def on_command_error(self, ctx, e):
        if self.bot.dev:
            await ctx.send(self.bot.loc("events_error_generic").format(
                t=type(e), e=e))
        else:
            if isinstance(e, commands.MissingRequiredArgument):
                await ctx.send(self.bot.loc("events_error_pmissing").format(e.param))
            elif isinstance(e, commands.NoPrivateMessage):
                await ctx.send(self.bot.loc("events_error_pmdisabled"))
            elif isinstance(e, commands.CommandOnCooldown):
                await ctx.send(self.bot.loc("events_error_cooldown").format(e.retry_after))
            elif isinstance(e, commands.NotOwner):
                await ctx.send(self.bot.loc("events_error_owneronly"))
            elif isinstance(e, commands.MissingPermissions):
                await ctx.send(self.bot.loc("events_error_u_cant"))
            elif isinstance(e, commands.BotMissingPermissions):
                await ctx.send(self.bot.loc("events_error_b_cant"))
            else:
                await ctx.send(self.bot.loc("events_error_undefined"))

def setup(bot):
    bot.add_cog(Events(bot))
