import asyncio,requests,json,random,config
from dataIOpy import js
from discord.ext import commands

class Tags():
    def __init__(self, bot):
        self.bot = bot
        self.config = js.load("config/tags.json")

    @commands.command()
    async def tag(self, ctx, *, tag : str = None):
        # El servidor tiene un album?
        try:
            x = self.config["albums"][str(ctx.message.guild.id)]
        except:
            await ctx.send("Este servidor no posee un album de Imgur registrado.")
            return
        # Solicitar el album del servidor
        req = requests.get("https://api.imgur.com/3/album/" + self.config["tags"][str(ctx.message.server.id)],
                           headers={"Authorization": "Client-ID " + config.imgur_client})
        # Asegurar la respuesta correcta
        if req.status_code != 200:
            await ctx.send("Ha ocurrido un error al obtener el album desde Imgur.")
            return
        # Agrupar correctamente los albumes
        par = json.loads(req.text)
        tags = [] # Lista de tags
        images = [] # Lista de imagenes
        for img in par["data"]["images"]:
            tags.append(img["description"].lower())
            images.append(img["link"])
        # Revisar si es que el tag esta o si se solicito la lista completa
        if tag in tags:
            tag = tag.lower()
            i = tags.index(tag)
        if tag == None:
            i = random.randrange(0, len(images))
        elif tag == "*":
            await ctx.send("Estos son los tags disponibles:\n" + ", ".join(tags))
            return
        else:
            await ctx.send("No se ha encontrado el Tag especificado, ¿estas seguro de que existe?")
            return
        await ctx.send(images[i])

def setup(bot):
    bot.add_cog(Tags(bot))
