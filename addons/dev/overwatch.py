import asyncio,logging,tools
import discord
from discord.ext import commands

class Overwatch():
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger("dva")
        self.cg = tools.get_json("data/customgames.json")

    @commands.group(pass_context=True)
    async def overwatch(self, ctx):
        if ctx.invoked_subcommand == None:
            await self.bot.say("Subcomandos: create/join/leave/delete/info/stats") # No se me ocurre ninguna mierda para colocar aqui

    @overwatch.command(pass_context=True)
    async def create(self, ctx, battletag : str, name : str, vs : str = None, description : str = None):
        # Revisar si el usuario ya ha creado una partida y esta guardada
        for cg in self.cg["cg"]:
            if cg["id"] == ctx.message.author.id:
                await self.bot.say("Ups, parece que ya has creado una partida personalizada.")
                return
        # Si no ha creado una, indexar el json para aplicarlo y guardarlo
        dict = { "id": ctx.message.author.id, "battletag": battletag, "name": name, "vs": vs, "description": description, "users": None}
        self.cg["cg"].append(dict)
        Tools.save_json("Data/CustomGames.json", self.cg)
        # Informar que la partida fue creada correctamente
        self.logger.info("Partida creada por \"{}\" en \"{}\"".format(ctx.message.user, ctx.message.server))
        await self.bot.say("Tu partida ha sido creada satisfactoriamente, ahora los jugadores pueden unirse a ella con el comando **{}join**. Puedes eliminarla con el comando **{}delete**.".format(ctx.prefix))

    @overwatch.command(pass_context=True)
    async def join(self, ctx, user):
        None

    @overwatch.command(pass_context=True)
    async def leave(self, ctx):
        None

    @overwatch.command(pass_context=True)
    async def delete(self, ctx):
        # Crear el array vacio y la variable
        ncg = []
        completed = False
        # Revisar cada uno de ellos
        for cg in self.cg["cg"]:
            # Si es que la id guardada es igual a la del autor guardar la variable y continuar
            if cg["id"] == ctx.message.author.id:
                completed = True
            # Si no es igual agragarla al array nuevamente
            else:
                ncg.append(cg)

        # Una vez que hayan sido completadas todas las operaciones ver que hacer
        # Si es que fue removido guardar y mostrar confirmacion
        if completed:
            self.cg = { "cg" : ncg }
            Tools.save_json("Data/CustomGames.json", self.cg)
            await self.bot.say("Se ha borrado la partida que has creado anteriormente.")
            self.logger.info("La partida de \"{}\" en \"{}\" ha sido eliminada".format(ctx.message.author, ctx.message.server))
        # Si es que no se encontro mostrar error
        else:
            await self.bot.say("Ups, parece que no has creado una partida.")

    @overwatch.command(pass_context=True)
    async def info(self, ctx, user : discord.User):
        None

def setup(bot):
    bot.add_cog(Overwatch(bot))
