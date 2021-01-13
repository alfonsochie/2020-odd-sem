import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os

TOKEN = 'Nzk4NTY2NTc2ODM1Mzk1NTg1.X_25FA.txUFHIGDTfEWd8n7COTU53rH2MM'
BOT_PREFIX = '!'

bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
    print("logged in as: " + bot.user.name + "\n")


@bot.command(pass_context=True, aliases=['j'])
async def join (ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"the bot has connected to {channel}\n")

    await ctx.send(f"joined {channel}")

@bot.command(pass_context=True, aliases=['l'])
async def leave(ctx):

    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"the bot has left {channel}")
        await ctx.send(f"left {channel}")
    else:
        print("bot was not in any voice channel")
        await ctx.send("I am not in a voice channel")

@bot.command(pass_context=True, aliases=['p'])
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("removed old song file")
    except PermissionError:
        print("The song is being played")
        await ctx.send("ERROR: Music playing")
        return

    await ctx.send("Getting ready")

    voice = get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith("mp3"):
            name = file
            print(f"Renamed file: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print(f"{name} has finished playing"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.3

    nname = name.rsplit("-",2)
    await ctx.send(f"Playing: {nname[0]}")
    print("Playing\n")

@bot.command(pass_context=True)
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")

@bot.command(pass_context=True, aliases=['r'])
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")

@bot.command(pass_context=True, aliases=['s'])
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()


bot.run(TOKEN)