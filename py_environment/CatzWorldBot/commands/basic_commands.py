import discord
from discord.ext import commands

class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Définition de la commande "hello"
    @commands.command(name="hello", help="Greets the user with a hello message.")
    async def hello(self, ctx, member: discord.Member):
        # Envoie du message de salutation
        await ctx.send(f"Hello {member.mention}!")

async def setup(bot):
    # Ajoute le cog au bot
    await bot.add_cog(BasicCommands(bot))
