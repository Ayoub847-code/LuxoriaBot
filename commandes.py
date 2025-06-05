import discord
from discord.ext import commands
from discord import app_commands
import json
import os

DATA_FILE = "database.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

class Commandes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="cmdencours", description="Voir les commandes en cours.")
    async def cmdencours(self, interaction: discord.Interaction):
        data = load_data()
        commandes = data.get("commandes", [])
        if not commandes:
            await interaction.response.send_message("❌ Aucune commande en cours.", ephemeral=True)
            return
        embed = discord.Embed(title="📦 Commandes en cours", color=0x00ffcc)
        for cmd in commandes:
            embed.add_field(name=cmd["produit"], value=f"Client: {cmd['client']} - Statut: {cmd['statut']}", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="addcmd", description="Ajouter une commande (admin seulement).")
    async def addcmd(self, interaction: discord.Interaction, client: str, produit: str):
        if interaction.user.id != 1072165245906333756:
            await interaction.response.send_message("❌ Tu n'as pas la permission.", ephemeral=True)
            return
        data = load_data()
        data.setdefault("commandes", []).append({
            "client": client, "produit": produit, "statut": "En attente"
        })
        save_data(data)
        await interaction.response.send_message("✅ Commande ajoutée.", ephemeral=True)

    @app_commands.command(name="progcmd", description="Marquer une commande comme en cours (admin).")
    async def progcmd(self, interaction: discord.Interaction, produit: str):
        data = load_data()
        modif = False
        for cmd in data.get("commandes", []):
            if cmd["produit"] == produit:
                cmd["statut"] = "En cours"
                modif = True
        save_data(data)
        await interaction.response.send_message("✅ Statut modifié." if modif else "❌ Produit non trouvé.", ephemeral=True)

    @app_commands.command(name="livrer", description="Marquer une commande comme livrée (admin).")
    async def livrer(self, interaction: discord.Interaction, produit: str):
        data = load_data()
        modif = False
        for cmd in data.get("commandes", []):
            if cmd["produit"] == produit:
                cmd["statut"] = "Livrée"
                modif = True
        save_data(data)
        await interaction.response.send_message("📦 Commande livrée !" if modif else "❌ Produit non trouvé.", ephemeral=True)

    @app_commands.command(name="supprcmd", description="Supprimer une commande (admin).")
    async def supprcmd(self, interaction: discord.Interaction, produit: str):
        data = load_data()
        before = len(data.get("commandes", []))
        data["commandes"] = [cmd for cmd in data.get("commandes", []) if cmd["produit"] != produit]
        save_data(data)
        await interaction.response.send_message("🗑️ Commande supprimée." if len(data["commandes"]) < before else "❌ Commande non trouvée.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Commandes(bot))