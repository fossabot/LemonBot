from discord.ext import commands
from addons.tools.ytdl import YTDLSource

class Player:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice.channel is not None:
            if ctx.voice_client is None:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.voice_client.move_to(ctx.author.voice.channel)
            await ctx.send(self.bot.loc("music_join_connected").format(
                ctx.author.voice.channel.name))
        else:
            await ctx.send(self.bot.loc("music_join_nope"))

    @commands.command()
    async def play(self, ctx, *, url: str):
        if ctx.voice_client is None:
            return await ctx.send(self.bot.loc("music_play_nope"))
        elif ctx.voice_client.is_playing():
            return await ctx.send(self.bot.loc("music_play_already"))

        player = await YTDLSource.from_url(url, loop=self.bot.loop)
        ctx.voice_client.play(
            player,
            after=lambda e: print(self.bot.loc("music_play_error").format(e)) if e else None
        )
        await ctx.send(self.bot.loc("music_play_now").format(player.title))

    @commands.command()
    async def volume(self, ctx, volume: int):
        if ctx.voice_client is None:
            return await ctx.send(self.bot.loc("music_volume_nope"))

        ctx.voice_client.source.volume = volume
        await ctx.send(self.bot.loc("music_volume_set").format(volume))

    @commands.command()
    async def stop(self, ctx):
        await ctx.voice_client.disconnect()

def setup(bot):
    bot.add_cog(Player(bot))
