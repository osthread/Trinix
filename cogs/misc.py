# ---------------------------------------------------------------- Required Imports ----------------------------------------------------------------

from discord.ext import commands, tasks
from random import choice

import discord, datetime, time, requests

# --------------------------------------------------------------------------------------------------------------------------------

class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# ---------------------------------------------------------------- Misc Commands ----------------------------------------------------------------

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'My Server Ping ({round(self.bot.latency * 1000)}ms)')

    @commands.command()
    async def oauth(self, ctx):
        responses = 'Heres my invite link https://discord.com/oauth2/authorize?client_id=985075081535451186&permissions=8&scope=bot%20applications.commands <3'
        await ctx.send(responses)
    
    @commands.command(aliases=['pwg'])
    async def passgen(self, ctx):
        API = "https://www.passwordrandom.com/query?command=password"
        x = requests.get(API)
        await ctx.author.send(x.text)

# --------------------------------------------------------------------------------------------------------------------------------

def setup(bot): #Must have a setup function
    bot.add_cog(misc(bot)) # Add the class to the cog.
