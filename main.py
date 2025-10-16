import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

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

# Evento: cuando el bot está listo
@bot.event
async def on_ready():
    print(f"Tamos ready, {bot.user.name}")

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

# ✅ Ejecutar el bot (siempre al final del archivo)
bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)