import discord
from discord.ext import commands
from discord import app_commands

class VIP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="addvip", description="Donne le rôle VIP à un utilisateur.")
    async def addvip(self, interaction: discord.Interaction, membre: discord.Member):
        vip_role = discord.utils.get(interaction.guild.roles, name="✨ VIP")
        if not vip_role:
            vip_role = await interaction.guild.create_role(name="✨ VIP")
        await membre.add_roles(vip_role)
        await interaction.response.send_message(f"✅ {membre.mention} est maintenant VIP !", ephemeral=True)

async def setup(bot):
    await bot.add_cog(VIP(bot))