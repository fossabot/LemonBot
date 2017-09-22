import sys
import os
import localize
from discord.ext.commands import Bot as LemonBot

try:
    import config
except ImportError:
    print("Config file not found.\nArchivo de Configuracion no encontrado.")
    sys.exit(1)

version = "1.0"
strings = localize.LocalizeMe("strings", config.lang)

def load_addons(bot):
    for addon in os.listdir("addons"):
        if addon.endswith(".py"):
            try:
                bot.load_extension("addons." + os.path.splitext(addon)[0])
            except Exception as e:
                print(strings.get("base_addon_error").format(addon=addon, type=type(e), error=e))

def start_bot():
    bot = LemonBot(command_prefix=config.prefix)
    bot.remove_command("help")
    load_addons(bot)
    bot.run(config.token)

if __name__ == "__main__":
    start_bot()
