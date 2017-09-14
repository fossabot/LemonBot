import discord,sys
from discord.ext import commands
from discord.ext.commands import Bot as LemonBot

version = "1.0" # Version para control interno
try: # Intentar importar la configuracion
    import config
except ImportError:
    print("No existe el archivo de configuracion.")
    sys.exit(1)

bot = LemonBot(command_prefix=config.prefix) # Crear el "Bot"

if __name__ == "__main__":
    bot.remove_command("help")
    for ext in config.startup:
        try: # Intentar cargar las extensiones
            bot.load_extension("addons." + ext)
        except e as Exception:
            print("Error al cargar {}: {} / {}".format(ext, type(e), e))
    bot.run(config.token)
