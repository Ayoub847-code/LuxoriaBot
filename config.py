import discord
from discord.ext import commands
from discord import app_commands

class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="config", description="Configurer les options du bot.")
    async def config(self, interaction: discord.Interaction):
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("❌ Tu dois être admin pour ça.", ephemeral=True)
            return
        embed = discord.Embed(title="⚙️ Configuration", description="Choisis ce que tu veux configurer :", color=0x3498db)
        view = discord.ui.View()
        view.add_item(discord.ui.Select(placeholder="Sélectionne une option", options=[
            discord.SelectOption(label="Système de tickets", value="tickets"),
            discord.SelectOption(label="Rôle VIP", value="vip"),
            discord.SelectOption(label="Salon Commandes", value="commandes")
        ]))
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

async def setup(bot):
    await bot.add_cog(Config(bot))