__title__ = "LemonBot"
__author__ = 'Lemon'
__license__ = "CC BY-NC-SA 4.0"
__copyright__ = "2016-2017 Lemon"
__version__ = "1.0-beta.1"

import os

if __name__ == "__main__":
    import logging
    import json
    import discord
    from discord.ext import commands

    class LemonBot(commands.Bot):
        "Base de LemonBot"
        def __init__(self, prefix: str = "&"):
            super().__init__(command_prefix=prefix)
            self.version = __version__
            self.name = __title__
            self.copy = __copyright__
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
            if os.environ.get("CI") == "true":
                print("Travis CI or AppVeyor Detected, Logging off...")
                await self.logout()

            print(self.loc("events_ready").format(
                un=self.user, id=self.user.id,
                gc=len(self.guilds), gu=len(self.users)))
            game = discord.Game(name=self.playing.format(
                v=self.version, g=len(self.guilds), p=self.prefix))
            await self.change_presence(game=game)

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
            with open("strings/" + lang + ".json") as of:
                text = of.read()
            j = json.loads(text)
            return j[string]

    bot = LemonBot()

    if os.environ.get("CI") == "true":
        bot.dev = True
        bot.load_extensions()
        bot.run(os.environ.get("DISCORD_TOKEN"))
    else:
        with open("config.json") as cfg:
            config = json.loads(cfg.read())

        bot.config = config
        bot.load_extensions()
        bot.run(config["tokens"]["discord"])
