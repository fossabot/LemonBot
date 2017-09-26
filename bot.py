import discord
from discord.ext import commands
from discord.ext.commands import Bot as LemonBot

try:
    import config
except:
    print("No se ha encontrado la configuracion, renombra \"template_config.py\" a \"config.py\" y editalo con la informacion correspondiente e intenta otra vez.")
    exit()

version = "0.1b"
bot = LemonBot(command_prefix=config.prefix)
print("Iniciando LemonBot v{}\n".format(version))

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name = "v" + version))
    
if __name__ == "__main__":
    bot.remove_command("help")
    for ext in config.startup:
        bot.load_extension("addons." + ext)

bot.run(config.token)
