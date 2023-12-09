import discord
from discord import app_commands
from discord.ext import tasks
import os
from keep_alive import keep_alive
import asyncio
from yt_dlp import YoutubeDL

client = discord.Client(intents=discord.Intents.default())
tree = discord.app_commands.CommandTree(client) #←ココ

@client.event
async def on_ready():
	print('ログインしました')
	myLoop.start()

@tree.command(name="join", description="neko's Music Botをボイスチャンネルに接続します")
async def join(interaction: discord.Interaction):
	if interaction.user.voice is None:
		await interaction.response.send_message("あなたはボイスチャンネルに接続していません。",ephemeral=True)
		return
	# ボイスチャンネルに接続する
	await interaction.user.voice.channel.connect()
	await interaction.response.send_message(f"ボイスチャンネル「<#{interaction.user.voice.channel.id}>」に接続しました。")

@tree.command(name="leave", description="neko's Music Botをボイスチャンネルから切断します")
async def leave(interaction: discord.Interaction):
	voice_client = interaction.guild.voice_client
	if voice_client is None:
		await interaction.response.send_message("neko's Music Botはボイスチャンネルに接続していません。",ephemeral=True)
		return
	await voice_client.disconnect()
	await interaction.response.send_message(f"ボイスチャンネル「<#{voice_client.channel.id}>」にから切断しました。")
	
final_filename = None
def yt_dlp_monitor(self, d):
    final_filename  = d.get('info_dict').get('_filename')
    # You could also just assign `d` here to access it and see all the data or even `print(d)` as it updates frequently

@tree.command(name="play", description="音楽を再生します")
async def play(interaction: discord.Interaction, url:str):
	voice_client = interaction.guild.voice_client
	if voice_client is None:
		await interaction.response.send_message("neko's Music Botはボイスチャンネルに接続していません。",ephemeral=True)
		return
	ydl_opts = {
		"format": "mp3/bestaudio/best",
		"postprocessors": [
			{
				"key": "FFmpegExtractAudio",
				"preferredcodec": "mp3",
			}
		],
		"progress_hooks": [yt_dlp_monitor]
	}
	with YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])
	await voice_client.play(discord.FFmpegPCMAudio(final_filename))
	await interaction.response.send_message("再生中")


@tree.command(name="stop", description="音楽を停止します")
async def play(interaction: discord.Interaction, url:str):
	voice_client = interaction.guild.voice_client
	if voice_client is None:
		await interaction.response.send_message("neko's Music Botはボイスチャンネルに接続していません。",ephemeral=True)
		return
	await voice_client.stop()
	await interaction.response.send_message("停止しました")


@tree.command(name="pause", description="音楽を一時停止します")
async def play(interaction: discord.Interaction, url:str):
	voice_client = interaction.guild.voice_client
	if voice_client is None:
		await interaction.response.send_message("neko's Music Botはボイスチャンネルに接続していません。",ephemeral=True)
		return
	await voice_client.pause()
	await interaction.response.send_message("停止しました")


@tree.command(name="resume", description="一時停止した音楽を再開します")
async def play(interaction: discord.Interaction, url:str):
	voice_client = interaction.guild.voice_client
	if voice_client is None:
		await interaction.response.send_message("neko's Music Botはボイスチャンネルに接続していません。",ephemeral=True)
		return
	await voice_client.resume()
	await interaction.response.send_message("再開しました")


@tasks.loop(seconds=20)  # repeat after every 10 seconds
async def myLoop():
	# work
	await client.change_presence(activity=discord.Game(
		name="☕猫の喫茶店でメイドとして勤務中 / https://discord.gg/aEEt8FgYBb"))
	await tree.sync()  #スラッシュコマンドを同期

TOKEN = os.getenv("DISCORD_TOKEN")
# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)
