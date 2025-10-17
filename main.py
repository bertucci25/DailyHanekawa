import discord
from discord.ext import commands, tasks
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


# Evento: cuando alguien se une al servidor
@bot.event
async def on_member_join(member):
    await member.send(f"Bienvenido {member.name}")

# Evento: cuando se recibe un mensaje
@bot.event
async def on_message(message):
    if message.author.bot:  # Ignorar cualquier bot
        return

    if "senjo" in message.content.lower():
        try:
            await message.delete()
            if message.channel.permissions_for(message.guild.me).send_messages:
                await message.channel.send(f"no se habla de bruno! - {message.author.mention}")
            else:
                print("❌ No tengo permiso para enviar mensajes en este canal.")
        except discord.Forbidden:
            print("❌ No tengo permiso para borrar o enviar mensajes.")
        except discord.HTTPException as e:
            print(f"❌ Error HTTP: {e}")

    await bot.process_commands(message)

# Lista de URLs de imágenes de Tsubasa Hanekawa
imagenes_tsubasa = [
    "imgs/1.jpeg",
    "imgs/hankwa2.png"
]

# ID del canal donde enviar las imágenes
CANAL_ID = 440013645502742560  # Reemplaza con el ID real de tu canal

# Evento: cuando el bot está listo
@bot.event
async def on_ready():
    print(f"✅ Bot listo como {bot.user}")
    subir_imagen_tsubasa.start()  # Inicia la tarea una vez que el bot esté listo

@tasks.loop(hours=24)
async def subir_imagen_tsubasa():
    canal = bot.get_channel(CANAL_ID)
    if canal:
        imagen_path = random.choice(imagenes_tsubasa)
        await canal.send("Hora de apreciar a Tsubasa Hanekawa 💜", file=discord.File(imagen_path))
        print(f"✅ Imagen enviada: {imagen_path}")
    else:
        print("❌ No se encontró el canal.")


# ✅ Ejecutar el bot (siempre al final del archivo)
bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)