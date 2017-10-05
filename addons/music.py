from discord.ext import commands
import config
import discord
import requests
from bs4 import BeautifulSoup

class Music():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lyrics(self, ctx, *, query : str):
        try:
            r = requests.get(
                url="https://api.genius.com/search?q=" + query,
                headers={"Authorization": "Bearer " + config.genius}
            ).json()["response"]["hits"][0]["result"]

            s = BeautifulSoup(requests.get(r["url"]).text, "html.parser")
            l = s.find("div", class_="lyrics").get_text().strip()

            embed = discord.Embed(
                title=self.bot.loc("music_lyrics_title").format(song=r["title_with_featured"]),
                description=l, url=r["url"])
            embed.set_thumbnail(url=r["header_image_thumbnail_url"])
        except IndexError:
            await ctx.send(self.bot.loc("music_lyrics_notfound").format(search=query))
        except discord.HTTPException:
            await ctx.send(self.bot.loc("music_lyrics_toobig").format(url=r["url"]))
        else:
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Music(bot))
    