import config
from addons.tools.localize import LocalizeMe
from discord.ext import commands

import genius
import discord
from monstercat.client import MonstercatFM

class Music():
    def __init__(self, bot):
        self.bot = bot
        self.strings = LocalizeMe("strings", config.lang)
        self.mcat = MonstercatFM("LemonBot by JustALemon")
        self.genius = genius.Genius(config.genius)

    @commands.command()
    async def lyrics(self, ctx, *, query : str):
        song = self.genius.search(query)
        lyrics = self.genius.lyrics(song)
        embed = discord.Embed(title=self.strings.get("music_lyrics_title").format(song=song.ftitle), description=lyrics, url=song.url)
        embed.set_thumbnail(url=song.cover)
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(self.strings.get("music_lyrics_toobig").format(url=song.url))

def setup(bot):
    bot.add_cog(Music(bot))
    