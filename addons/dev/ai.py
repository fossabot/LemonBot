import asyncio,logging,random,discord
from dataIOpy import js
from discord.ext import commands

class AI():
    def __init__(self, bot):
        self.bot = bot
        self.config = js.load("config/ai.json")

    async def on_message(self, message):
        # Asegurarse que el Bot no responde a si mismo, si no se abre la caja de pandora
        if message.author == self.bot.user: return
        # Asegurarse de que el Bot esta en un canal permitido
        valid = False
        for chan in self.config["channels"]:
            if chan == message.channel.id:
                valid = True
                break
        # Si no, volver
        if valid == False: return
        # Estos son los tipos de mensajes y el tipo por defecto
        msgtypes = [ "saludos", "insultos", "agradecimientos", "chistes" ]
        msgtype = "random"
        # Revisar que es y enviar la respuesta que corresponda
        for t in msgtypes:
            if check_type(message, self.config["preguntas"][t]):
                msgtype = t
                break
        # Enviar un mensaje random de acuerdo al tipo de texto
        await message.channel.send(random.choice(self.config["respuestas"][msgtype]))
        # Y guardarlo si es de mas de 10 caracteres
        if len(message.content) >= 10:
            self.config["respuestas"][msgtype].append(message.content)
            js.dump(self.config, "config/ai.json", overwrite=True, indent_format=True, enable_verbose=False)

def check_type(uinput, cfg):
    valid = False
    for txt in cfg:
        if txt.lower() in uinput.content.lower():
            return True

def setup(bot):
    bot.add_cog(AI(bot))
