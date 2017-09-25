import discord
import asyncio
from youtube_dl import YoutubeDL

ytdl_options = {
    "format": "bestaudio/best",
    "outtmpl": "music/%(extractor)s-%(id)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto"
}

ffmpeg_options = {
    "before_options": "-nostdin",
    "options": "-vn"
}

ytdl = YoutubeDL(ytdl_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.75):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get("title")
        self.url = data.get("url")

    @classmethod
    async def from_url(cls, url, *, loop=None):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, ytdl.extract_info, url)
        if "entries" in data:
            data = data["entries"][0]
        filename = ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)
