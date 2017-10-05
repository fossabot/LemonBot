from discord.ext import commands
import discord

class Events():
    def __init__(self, bot):
        self.bot = bot
        self.base = "v{} | {} Guilds | {}help"

    async def on_ready(self):
        print("Conectado a Discord!")
        print("Usuario: {} / {}".format(self.bot.user, self.bot.user.id))
        print("Guilds: {} ({} Usuarios)".format(len(self.bot.guilds), len(self.bot.users)))
        game = discord.Game(name=self.base.format(
            self.bot.version, len(self.bot.guilds), self.bot.prefix)
        )
        await self.bot.change_presence(game=game)

    async def on_command_error(self, ctx, error):
        if self.bot.dev:
            await ctx.send(self.bot.loc("eh_error_occurred") +
                           "\n```{}: {}\n```".format(type(error), error))
        else:
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send(self.bot.loc("eh_param_missing").format(param=error.param))
            elif isinstance(error, commands.NoPrivateMessage):
                await ctx.send(self.bot.loc("eh_private_disabled"))
            elif isinstance(error, commands.CommandOnCooldown):
                await ctx.send(self.bot.loc("eh_on_cooldown").format(seg=error.retry_after))
            elif isinstance(error, commands.NotOwner):
                await ctx.send(self.bot.loc("eh_owner_only"))
            elif isinstance(error, commands.MissingPermissions):
                await ctx.send(self.bot.loc("eh_user_not_allowed"))
            elif isinstance(error, commands.BotMissingPermissions):
                await ctx.send(self.bot.loc("eh_bot_not_allowed"))
            else:
                await ctx.send(self.bot.loc("eh_not_defined"))

def setup(bot):
    bot.add_cog(Events(bot))
