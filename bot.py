import sys
import localize
from discord.ext.commands import Bot as LemonBot

try:
    import config
except ImportError:
    print("Config file not found.\nArchivo de Configuracion no encontrado.")
    sys.exit(1)

version = "1.0"
strings = localize.LocalizeMe("strings", config.lang)

def load_addon(bot, addon):
    try:
        bot.load_extension("addons." + addon)
    except Exception as e:
        print(strings.get("base_addon_error").format(addon=addon, type=type(e), error=e))

def start_bot():
    bot = LemonBot(command_prefix=config.prefix)
    bot.remove_command("help")
    startup = ["error_handler", "music", "owner_tools"]
    for ext in startup:
        load_addon(bot, ext)
    bot.run(config.token)

if __name__ == "__main__":
    start_bot()
