__title__ = "LemonBot"
__author__ = 'Lemon'
__license__ = "CC BY-NC-SA 4.0"
__copyright__ = "2016-2017 Lemon"
__version__ = "1.0-beta.1"

import sys
import os

sys.path.append(os.path.abspath(".."))

if __name__ == "__main__":
    import logging
    import json
    import config
    from discord.ext import commands

    class LemonBot(commands.Bot):
        "Base de LemonBot"
        def __init__(self, prefix: str):
            super().__init__(command_prefix=prefix)
            self.version = __version__
            self.name = __title__
            self.copy = __copyright__
            self.lang = "es-CL"
            self.dev = False
            self.web = "http://bot.justalemon.ml"
            self.help = self.web + "/commands.html"
            self.repo = "https://github.com/Lemon-CL/LemonBot"
            self.log = logging.getLogger(self.name)
            self.database = None # Porcia
            self.prefix = prefix

            self.remove_command("help")

            for addon in os.listdir("addons"):
                if addon.endswith(".py"):
                    addon_name = os.path.splitext(addon)[0]
                    try:
                        self.load_extension("addons." + addon_name)
                    except Exception as e:
                        print("Error loading {}: {} / {}".format(addon, type(e), e))

        def loc(self, string: str, lang: str = None):
            if lang is None:
                lang = self.lang
            with open("strings/" + lang + ".json") as of:
                text = of.read()
            j = json.loads(text)
            return j[string]

    bot = LemonBot(config.prefix)
    bot.run(config.token)
