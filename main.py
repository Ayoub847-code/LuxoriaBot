import discord
from discord.ext import commands
import os
import json

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

OWNER_ID = 1072165245906333756

@bot.event
async def on_ready():
    print(f"✅ {bot.user} est en ligne.")
    for guild in bot.guilds:
        await setup_guild(guild)

async def setup_guild(guild):
    existing = discord.utils.get(guild.text_channels, name="commandes")
    if not existing:
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True)
        }
        channel = await guild.create_text_channel("commandes", overwrites=overwrites)
        await channel.send("📦 Voici les commandes en cours ou livrées.")
    else:
        print(f"Salon #commandes déjà existant dans {guild.name}")

@bot.event
async def on_guild_join(guild):
    await setup_guild(guild)

# Chargement des cogs
cogs = ['boutique', 'commandes', 'admin', 'config', 'tickets', 'vip']

for cog in cogs:
    try:
        bot.load_extension(cog)
        print(f"🔄 {cog}.py chargé.")
    except Exception as e:
        print(f"Erreur en chargeant {cog}: {e}")

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
bot.run(TOKEN)