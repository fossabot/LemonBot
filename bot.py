import sys
import os

version = "1.0-beta.1"
name = "LemonBot"
copy = "2017 Lemon"
webpage = "http://bot.justalemon.ml"
bhelp = "http://bot.justalemon.ml/commands.html"
repo = "https://github.com/Lemon-CL/LemonBot"

sys.path.append(os.path.abspath(".."))

def load_addons(bot):
    """Carga los archivos de Python desde \"addons\""""
    for addon in os.listdir("addons"):
        if addon.endswith(".py"):
            try:
                bot.load_extension("addons." + os.path.splitext(addon)[0])
            except ImportError as e:
                print("Error loading {}: {} / {}".format(addon, type(e), e))

def start_bot():
    """Inicia al Bot normalmente"""
    try:
        import config
    except ImportError:
        print("Configuration file not found.")
        sys.exit(1)

    from discord.ext.commands import Bot as LemonBot
    bot = LemonBot(command_prefix=config.prefix)
    bot.remove_command("help")
    load_addons(bot)
    bot.run(config.token)

if __name__ == "__main__":
    start_bot()
