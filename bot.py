__title__ = "LemonBot"
__author__ = 'Lemon'
__license__ = "CC BY-NC-SA 4.0"
__copyright__ = "2016-2017 Lemon"
__version__ = "1.0-beta.1"

import os
import json

if __name__ == "__main__":
    from customclass import LemonBot
    BOT = LemonBot()

    if os.environ.get("CI") in ["true", "True"]:
        BOT.dev = True
        BOT.load_extensions()
        BOT.run(os.environ.get("DISCORD_TOKEN"))
    else:
        with open("config.json") as cfg:
            CONFIG = json.loads(cfg.read())

        BOT.config = CONFIG
        BOT.load_extensions()
        BOT.run(CONFIG["tokens"]["discord"])
