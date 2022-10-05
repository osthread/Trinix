# ---------------------------------------------------------------- Required Imports ----------------------------------------------------------------
from discord.ext import commands, tasks
from discord import message

import discord

# --------------------------------------------------------------------------------------------------------------------------------

class listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):# Error Listener
            embed=discord.Embed(title="[Trinix Error System]", description="[ERROR]You are missing requirements.", color=0xff0000)
            await ctx.send(embed=embed)

        if isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(title="Trinix Error System", description="[EEROR]You do not have the required permissions.", color=0xff0000)
            await ctx.send(embed=embed)

def setup(bot): #Must have a setup function
        bot.add_cog(listener(bot)) # Add the class to the cog.

# --------------------------------------------------------------------------------------------------------------------------------

