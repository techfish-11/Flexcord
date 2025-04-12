import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="help", description="Flexcord Help")
    async def help_command(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Welcome to Flexcord!!",
            description=(
                "Flexcord is a bot that lets you use Discord more freely and creatively. Easily customize your bot and add features tailored to your server. With an intuitive interface, you can configure the bot's behavior using YAML files and instantly update it to your server.\n\n"
                "[Here is the bot status(comming soon)](https://status.sakana11.org/)\n"
            ),
            color=discord.Color.yellow()
        )

        embed.add_field(
            name="how to use",
            value=(
                "1. Access to [Flexcord](https://flexcord.sakana11.org/) and login with your Discord account.\n"
                "2. Select the server you want to customize.\n"
                "3. Write scripts to customize using YAML. \n"
                "4. Upload the script and it will be applied to your server.\n"),
            inline=False
        )

        embed.set_footer(
            text="https://sakana11.org/Flexcord"
        )

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))