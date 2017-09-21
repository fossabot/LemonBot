import config
import localize
from discord.ext import commands

import genius
import discord
import youtube_dl
from tools.discord_ytdl import YTDLSource

class Music():
    def __init__(self, bot):
        self.bot = bot
        self.strings = localize.LocalizeMe("strings", config.lang)
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
            await ctx.send(self.strings.get("music_lyrics_toobig"))

    @commands.group()
    async def music(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send(self.strings.get("music_base_subcommand_none"))

    @music.command()
    async def join(self, ctx):
        if ctx.author.voice.channel is not None:
            if ctx.voice_client is not None:
                await ctx.voice_client.move_to(ctx.author.voice.channel)
            else:
                await ctx.author.voice.channel.connect()
            await ctx.send(self.strings.get("music_join_connected").format(channel=ctx.voice_client.channel.name))
        else:
            await ctx.send(self.strings.get("music_channel_nope"))

    @music.command()
    async def play(self, ctx, *, url : str):
        if ctx.voice_client is None:
            return await ctx.send(self.strings.get("music_channel_nope"))

        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()

        player = await YTDLSource.from_url(url, loop=self.bot.loop)
        ctx.voice_client.play(player, after=lambda e: print(self.strings.get("music_play_error").format(e)) if e else None)
        
        await ctx.send(self.strings.get("music_play_now").format(song=player.title))

    @music.command()
    async def volume(self, ctx, volume : int):
        if ctx.voice_client is None:
            return await ctx.send(self.strings.get("music_channel_nope"))

        ctx.voice_client.source.volume = volume
        await ctx.send(self.strings.get("music_volume_set").format(volume=volume))

    @music.command()
    async def stop(self, ctx):
        await ctx.voice_client.disconnect()

def setup(bot):
    bot.add_cog(Music(bot))
    