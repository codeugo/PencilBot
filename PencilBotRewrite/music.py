import discord
import json
from discord.ext import commands
from discord import slash_command
import asyncio

with open('json/config.json') as jsondata:
    config = json.load(jsondata)

class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[config['serverid']])
    async def join(self, ctx,name: str = None):
        name = name or ctx.author.name
        if ctx.author.voice is None:
            await ctx.respond(f"Tu n'es pas dans un channel vocal.")
        if ctx.voice_client is None:
            voice_channel = ctx.author.voice.channel
            await voice_channel.connect()
            await ctx.respond(f"Rejoint le channel vocal de **{name}**.")
        else:
            voice_channel = ctx.author.voice.channel
            await ctx.voice_client.move_to(voice_channel)
            await ctx.respond(f"Rejoint le channel vocal de **{name}**.")
    
    @slash_command(guild_ids=[config['serverid']])
    async def disconnect(self,ctx,name: str = None):
        name = name or ctx.author.name
        await ctx.voice_client.disconnect()
        await ctx.respond(f"Quitté le channel vocal de **{name}**.")

    @slash_command(guild_ids=[config['serverid']])
    async def play(self,ctx,url,name: str = None):
        name = name or ctx.author.name
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            await ctx.respond("Téléchargement de l'audio...")
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            video_title = info.get('title', None)
            vc.play(source)
        
        await ctx.send(f"En train de jouer `{video_title}` dans le channel vocal de **{name}**.")

    @slash_command(guild_ids=[config['serverid']])
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.respond(f"Musique mis en pause.")
        

    @slash_command(guild_ids=[config['serverid']])
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.respond(f"Musique repris.")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
    
        if not member.id == self.bot.user.id:
            return

        elif before.channel is None:
            voice = after.channel.guild.voice_client
            time = 0
            while True:
                await asyncio.sleep(1)
                time = time + 1
                if voice.is_playing() and not voice.is_paused():
                    time = 0
                if time == 60:
                    await voice.disconnect()
                if not voice.is_connected():
                    break

def setup(bot):
    bot.add_cog(music(bot))