#Required Imports
import discord 
from discord import message
from discord.ext import commands, tasks

class listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()#This will tell you is you are missing perms / req
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('you are missing requirements :rolling_eyes:.')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You dont have all the required permissions :angry:")

def setup(bot): #Must have a setup function
        bot.add_cog(listener(bot)) # Add the class to the cog.