import asyncio,logging
from dataIOpy import js
from discord.ext import commands

class NewMembers:
    def __init__(self, bot):
        self.bot = bot
        self.config = js.load("config/newmembers.json")

    async def on_member_join(self, member):
        try:
            await member.send(self.config["messages"][str(member.guild.id)].format(user = member.mention,
                                                                                    server = member.guild,
                                                                                    n = "\n"))
        except:
            return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def welcome(self, ctx, *, message : str = None):
        if message == "delete" or message == "remove":
            del self.config["messages"][str(ctx.message.guild.id)]
            await ctx.send("Aviso de bienvenida eliminado.")
        elif message != None:
            self.config["messages"][str(ctx.message.guild.id)] = message
            await ctx.send("Mensaje de bienvenida añadido/cambiado.")
        else:
            try:
                await ctx.send("Mensaje de bienvenida:\n" + self.config["messages"][str(ctx.message.guild.id)])
            except:
                await ctx.send("El servidor no posee un mensaje de bienvenida.")
            return
        js.dump(self.config, "config/newmembers.json", overwrite=True, indent_format=True, enable_verbose=False)

def setup(bot):
    bot.add_cog(NewMembers(bot))
    