import discord
from discord.ext import commands, tasks
import logging
from dotenv import load_dotenv
import os
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='&', intents=intents)

@bot.event
async def on_ready():
    print(f"Tamos ready, {bot.user.name}")

@bot.event
async def on_member_join(member):
    await member.send(f"Bienvenido {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "senjo" in message.content.lower():
        await message.delete()

        if message.channel.permissions_for(message.guild.me).send_messages:
            await message.channel.send(f"no se habla de bruno! - {message.author.mention}")

    await bot.process_commands(message)

# Lista de URLs de imágenes de Tsubasa Hanekawa
imagenes_tsubasa = [
    "https://images4.alphacoders.com/826/thumb-1920-826754.jpg",
    "https://images6.alphacoders.com/983/thumb-1920-983544.jpg",
    "https://images2.alphacoders.com/108/thumb-1920-1088410.jpg",
    "https://images6.alphacoders.com/392/thumb-1920-392309.jpg",
    "https://images4.alphacoders.com/213/thumb-1920-213316.jpg",
    "https://images8.alphacoders.com/826/thumb-1920-826921.png",
    "https://images4.alphacoders.com/724/thumb-1920-724931.png",
    "https://images.alphacoders.com/455/thumb-1920-455318.jpg",
    "https://images2.alphacoders.com/109/thumb-1920-1096026.jpg",
    "https://images7.alphacoders.com/742/thumb-1920-742134.png"
]

# ID del canal donde enviar las imágenes
CANAL_ID = 440013645502742560  # Reemplaza con el ID real de tu canal

@bot.event
async def on_ready():
    print(f"✅ Bot listo como {bot.user}")
    subir_imagen_tsubasa.start()  # Inicia la tarea una vez que el bot esté listo

@tasks.loop(hours=24)
async def subir_imagen_tsubasa():
    canal = bot.get_channel(CANAL_ID)
    if canal:
        url = random.choice(imagenes_tsubasa)
        await canal.send("Hora de apreciar a la waifu 💜", file=discord.File(await descargar_imagen(url), filename="tsubasa.jpg"))
    else:
        print("❌ No se encontró el canal.")

async def descargar_imagen(url):
    import aiohttp
    import io
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                raise Exception(f"Error al descargar la imagen: {resp.status}")
            data = await resp.read()
            return io.BytesIO(data)

bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)
