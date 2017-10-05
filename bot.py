import sys
import os
import logging
import json
import config
from discord.ext import commands

sys.path.append(os.path.abspath(".."))

class LemonBot(commands.Bot):
    "Base de LemonBot"
    def __init__(self):
        super().__init__(command_prefix=config.prefix)
        self.version = "1.0-beta.1"
        self.name = "LemonBot"
        self.copy = "2017 Lemon"
        self.lang = config.lang
        self.dev = config.dev
        self.web = "http://bot.justalemon.ml"
        self.help = self.web + "/commands.html"
        self.repo = "https://github.com/Lemon-CL/LemonBot"
        self.log = logging.getLogger(self.name)
        self.db = None # Porcia}
        self.prefix = config.prefix

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

if __name__ == "__main__":
    bot = LemonBot()
    bot.run(config.token)
