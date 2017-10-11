import os
import logging
import json
import bot
import discord
from discord.ext import commands

class LemonBot(commands.Bot):
    "Base de LemonBot"
    def __init__(self, prefix: str = "&"):
        super().__init__(command_prefix=prefix)
        self.version = bot.__version__
        self.name = bot.__title__
        self.copy = bot.__copyright__
        self.lang = "es-CL"
        self.config = None
        self.dev = False
        self.playing = "v{v} | {g} Guilds | {p}help"
        self.web = "http://bot.justalemon.ml"
        self.help = self.web + "/commands.html"
        self.repo = "https://github.com/Lemon-CL/LemonBot"
        self.log = logging.getLogger(self.name)
        self.database = None # Porcia
        self.prefix = prefix

        self.remove_command("help")

    async def on_ready(self):
        """Acciones al completarse el inicio de sesion."""
        if os.environ.get("CI") in ["true", "True"]:
            print("Travis CI or AppVeyor Detected, Logging off...")
            await self.logout()
        else:
            print(self.loc("events_ready").format(
                un=self.user, id=self.user.id,
                gc=len(self.guilds), gu=len(self.users)))
            game = discord.Game(name=self.playing.format(
                v=self.version, g=len(self.guilds), p=self.prefix))
            await self.change_presence(game=game)

    async def on_command_error(self, ctx, error):
        """Mensajes a la hora de Generarse un Error."""
        if self.dev:
            await ctx.send(self.loc("events_error_development").format(
                t=type(error), e=error))
        else:
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send(self.loc("events_error_pmissing").format(error.param))
            elif isinstance(error, commands.NoPrivateMessage):
                await ctx.send(self.loc("events_error_pmdisabled"))
            elif isinstance(error, commands.CommandOnCooldown):
                await ctx.send(self.loc("events_error_cooldown").format(error.retry_after))
            elif isinstance(error, commands.NotOwner):
                await ctx.send(self.loc("events_error_owneronly"))
            elif isinstance(error, commands.MissingPermissions):
                await ctx.send(self.loc("events_error_u_cant"))
            elif isinstance(error, commands.BotMissingPermissions):
                await ctx.send(self.loc("events_error_b_cant"))
            else:
                await ctx.send(self.loc("events_error_generic"))

    def load_extensions(self):
        """Carga los Addons o Cogs desde el directorio respectivo."""
        for addon in os.listdir("addons"):
            if addon.endswith(".py"):
                addon_name = os.path.splitext(addon)[0]
                self.load_extension("addons." + addon_name)

    def loc(self, string: str, lang: str = None):
        """Carga un string en un idioma especifico."""
        if lang is None:
            lang = self.lang
        with open("strings/" + lang + ".json") as open_file:
            text = open_file.read()
        lines = json.loads(text)
        return lines[string]
