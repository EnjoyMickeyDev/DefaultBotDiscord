import disnake
from disnake.ext import commands

from core.defaultbotdiscord import DefaultBotDiscord

class Developer(commands.Cog):
    def __init__(self, bot):
        self.bot: DefaultBotDiscord = bot

    @commands.slash_command(name='DefaultBotDiscord')
    async def DefaultBotDiscord(
        self, 
        interaction: disnake.GuildCommandInteraction
        ):
        embed = disnake.Embed()

        await interaction.response.defer(
            ephemeral=True
            )

        embed.description = "DefaultBotDiscord"

        await interaction.send(
            embed=embed
            )
def setup(bot):
    bot.add_cog(Developer(bot))