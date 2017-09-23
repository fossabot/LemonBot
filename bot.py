import sys
import os

try:
    import config
except ImportError:
    print("Configuration file not found.")
    sys.exit(1)

version = "1.0"

def load_addons(bot):
    for addon in os.listdir("addons"):
        if addon.endswith(".py"):
            try:
                bot.load_extension("addons." + os.path.splitext(addon)[0])
            except ImportError as e:
                print("Error loading {}: {} / {}".format(addon, type(e), e))

def start_bot():
    from discord.ext.commands import Bot as LemonBot
    bot = LemonBot(command_prefix=config.prefix)
    bot.remove_command("help")
    load_addons(bot)
    bot.run(config.token)

if __name__ == "__main__":
    start_bot()
