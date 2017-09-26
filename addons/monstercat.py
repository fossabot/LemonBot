import asyncio,json,requests,discord,time
from dataIOpy import js
from discord.ext import commands

class MonstercatFM():
    def __init__(self, bot):
        self.bot = bot
        self.config = js.load("config/monstercat.json")

    @commands.command()
    async def fm(self, ctx):
        # Solicitar las canciones
        req = requests.get("https://prism.theak.io/api/v3/tracklist?origin=LemonBot&l=1")
        if req.status_code != 200:
            await ctx.send("No se ha podido obtener la cancion actual, la API no respondio de manera correcta.")
            return
        data = json.loads(req.text)
        # Crear el Embed para mostrar la informacion
        embed = discord.Embed(colour=discord.Colour(0x6E6E6E), url=self.config["stream"])
        embed.set_author(name="Cancion actual en Monstercat FM", icon_url="https://assets.monstercat.com/essentials/logos/monstercat_logo_square_small.png")
        # Mostrar pequeño o grande
        if self.config["thumbnail"]:
            embed.set_thumbnail(url=data["tracks"][0]["album_cover"])
        else:
            embed.set_image(url=data["tracks"][0]["album_cover"])
        # Añadir la informacion
        embed.add_field(name="Nombre", value=data["tracks"][0]["title"])
        embed.add_field(name="Artista", value=data["tracks"][0]["artists"][0]["name"])
        embed.add_field(name="Album", value=data["tracks"][0]["album_name"])
        embed.add_field(name="Duracion", value=time.strftime("%H:%M:%S", time.gmtime(data["tracks"][0]["track_duration"])))
        embed.add_field(name="Reproducida a las", value=time.strftime('%H:%M:%S', time.localtime(data["tracks"][0]["time"] / 1000)) + " GMT -4")
        # Enviarlo
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(MonstercatFM(bot))
