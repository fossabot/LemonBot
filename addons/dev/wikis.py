import asyncio,logging,json
import discord,requests,WikiaLib
import requests,json
from discord.ext import commands

class Wikis():
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger("lemon")
        self.config = json.load(open("config/wikis.json"))

    @commands.command(pass_context=True)
    async def wikia(self, ctx, lang : str, wiki : str, *, search : str):
        try:
            client = WikiaLib.Wikia(wiki)
            client.set_lang(lang)
            s = client.search(search)
            a = client.get_article(s[0])
        except WikiaLib.RequestError:
            await self.bot.say("Ups, parece que la wiki seleccionada no es valida. Asegurate que el codigo de idioma y el nombre de la wiki sean correctos e intenta nuevamente.")
        else:
            e = discord.Embed(title="Resultado de la busqueda de {} en {} Wiki.".format(search, wiki), description=a)

            self.logger.info("Info de \"{}\" solicitada desde \"{}\" por \"{}\" en \"{}\"".format(search, lang + "." + wiki, ctx.message.author, ctx.message.server))
            await self.bot.say(embed=e)

def setup(bot):
    bot.add_cog(Wikis(bot))
