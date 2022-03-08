#Required Imports
from discord import message
from discord.ext import commands, tasks

import discord


class listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()#This will tell you is you are missing perms / req
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            message = "you are missing requirements"
            embed=discord.Embed(title="Trinix Mod System", description=message, color=0xff0000)
            await ctx.send(embed=embed)

        if isinstance(error, commands.MissingPermissions):
            message = "You dont have all the required permissions"
            message = "you are missing requirements"
            embed=discord.Embed(title="Trinix Mod System", description=message, color=0xff0000)
            await ctx.send(embed=embed)

def setup(bot): #Must have a setup function
        bot.add_cog(listener(bot)) # Add the class to the cog.
