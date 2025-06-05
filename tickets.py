import discord
from discord.ext import commands
from discord import app_commands

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ticket_category = None

    @app_commands.command(name="ticket", description="Ouvre un ticket pour contacter le staff.")
    async def ticket(self, interaction: discord.Interaction):
        guild = interaction.guild
        category = discord.utils.get(guild.categories, name="🎫 Tickets")
        if not category:
            category = await guild.create_category("🎫 Tickets")
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            guild.me: discord.PermissionOverwrite(read_messages=True)
        }
        channel = await guild.create_text_channel(name=f"ticket-{interaction.user.name}", overwrites=overwrites, category=category)
        await channel.send(f"{interaction.user.mention}, un membre du staff va bientôt répondre à ta demande.")
        await interaction.response.send_message(f"✅ Ticket ouvert : {channel.mention}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Tickets(bot))