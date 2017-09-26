import asyncio,logging
from dataIOpy import js
from discord.ext import commands

class Config():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=[ "cfg" ])
    @commands.has_permissions(administrator=True)
    async def config(self, ctx, config : str, par1 : str = None, par1 : str = None):
        if config == "album":
            data = js.load("config/tags.json")
            if par1 == None:
                try:
                    await ctx.send("https://imgur.com/a/{}".format())
                except:
                    await ctx.send("Este servidor no posee un album de Imgur registrado.")
            elif par1 == "delete" or par1 == "remove":
                try:
                    del data["albums"][str(ctx.message.guild.id)]
                except:
                    await ctx.send("Este servidor no posee un album de Imgur registrado.")
                else:
                    await ctx.send ("Album eliminado satisfactoriamente.")
            else:
                data["albums"][str(ctx.message.guild.id)] = str
                js.dump(data)

def setup(bot):
    bot.add_cog(Config(bot))
