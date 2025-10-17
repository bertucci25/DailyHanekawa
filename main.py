import discord
from discord.ext import commands, tasks
from keep_alive import keep_alive
import logging
from dotenv import load_dotenv
import os
import random

# Cargar el token desde .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Logging a archivo
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Intents necesarios
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Inicializar el bot
bot = commands.Bot(command_prefix='&', intents=intents)

# ID del canal donde enviar las imágenes
CANAL_ID = 440013645502742560  # Reemplaza con tu canal real

# Carpeta donde están las imágenes
IMAGENES_DIR = "imgs"

# Evento: cuando el bot está listo
@bot.event
async def on_ready():
    print(f"✅ Bot listo como {bot.user}")
    subir_imagen_tsubasa.start()

@tasks.loop(hours=24)
async def subir_imagen_tsubasa():
    canal = bot.get_channel(CANAL_ID)
    if not canal:
        print("❌ No se encontró el canal.")
        return

    # Filtra solo archivos válidos (jpg, png, etc.)
    imagenes = [f for f in os.listdir(IMAGENES_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    if not imagenes:
        print("⚠️ No hay imágenes en la carpeta.")
        return

    imagen_elegida = random.choice(imagenes)
    ruta_completa = os.path.join(IMAGENES_DIR, imagen_elegida)

    await canal.send("Hora de apreciar a Hanekawa 💜", file=discord.File(ruta_completa))
    print(f"✅ Imagen enviada: {ruta_completa}")


keep_alive()

# ✅ Ejecutar el bot (siempre al final del archivo)
bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)