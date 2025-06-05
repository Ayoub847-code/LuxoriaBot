import discord
from discord.ext import commands
from discord import app_commands

class Boutique(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="acheter", description="Acheter un produit dans la boutique.")
    async def acheter(self, interaction: discord.Interaction):
        embed = discord.Embed(title="🛍️ Boutique Luxoria", description="Choisis une catégorie :", color=0x00ffcc)
        view = discord.ui.View()
        buttons = [
            ("Tools", "🛠️"), ("Serveurs", "🌐"), ("Bots", "🤖"),
            ("Logos", "🎨"), ("Nitro", "⚡")
        ]
        for label, emoji in buttons:
            view.add_item(discord.ui.Button(label=label, style=discord.ButtonStyle.primary, emoji=emoji, custom_id=f"cat_{label.lower()}"))
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

async def setup(bot):
    await bot.add_cog(Boutique(bot))