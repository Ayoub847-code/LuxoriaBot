import discord
from discord.ext import commands
from discord import app_commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="say", description="Faire parler le bot (admin seulement).")
    async def say(self, interaction: discord.Interaction, message: str):
        if interaction.user.id != 1072165245906333756:
            await interaction.response.send_message("❌ Tu n'as pas la permission.", ephemeral=True)
            return
        await interaction.channel.send(message)
        await interaction.response.send_message("✅ Message envoyé.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Admin(bot))