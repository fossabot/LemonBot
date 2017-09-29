import config
from addons.tools.localize import LocalizeMe
from discord.ext import commands

class Events():
    def __init__(self, bot):
        self.bot = bot
        self.strings = LocalizeMe("strings", config.lang)

    async def on_command_error(self, ctx, error):
        if config.dev:
            await ctx.send(self.strings.get("eh_error_occurred") + "\n```{}: {}\n```".format(type(error), error))
        else:
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send(self.strings.get("eh_param_missing").format(param=error.param))
            elif isinstance(error, commands.NoPrivateMessage):
                await ctx.send(self.strings.get("eh_private_disabled"))
            elif isinstance(error, commands.CommandOnCooldown):
                await ctx.send(self.strings.get("eh_on_cooldown").format(seg=error.retry_after))
            elif isinstance(error, commands.NotOwner):
                await ctx.send(self.strings.get("eh_owner_only"))
            elif isinstance(error, commands.MissingPermissions):
                await ctx.send(self.strings.get("eh_user_not_allowed"))
            elif isinstance(error, commands.BotMissingPermissions):
                await ctx.send(self.strings.get("eh_bot_not_allowed"))
            else:
                await ctx.send(self.strings.get("eh_not_defined"))

def setup(bot):
    bot.add_cog(Events(bot))
