from discord.ext import commands
import discord
import aiohttp
import requests
from bs4 import BeautifulSoup

class Music():
    def __init__(self, bot):
        self.bot = bot
        self.gurl = "https://api.genius.com/search?q={}"
        self.gauth = {"Authorization": "Bearer " + self.bot.config["tokens"]["genius"]}

    @commands.command()
    async def lyrics(self, ctx, *, query : str):
        url = "https://api.genius.com/search?q=" + query
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=self.gauth) as resp:
                    res = await resp.json()
                    song = res["response"]["hits"][0]["result"]
            soup = BeautifulSoup(requests.get(song["url"]).text, "html.parser")
            lyric = soup.find("div", class_="lyrics").get_text().strip()

            embed = discord.Embed(
                title=self.bot.loc("music_lyrics_title").format(song["title_with_featured"]),
                description=lyric, url=song["url"])
            embed.set_thumbnail(url=song["header_image_thumbnail_url"])
        except IndexError:
            await ctx.send(self.bot.loc("music_lyrics_notfound").format(query))
        except discord.HTTPException:
            await ctx.send(self.bot.loc("music_lyrics_toobig").format(song["url"]))
        else:
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Music(bot))
    