# ---------------------------------------------------------------- Required Imports ----------------------------------------------------------------

from discord.ext import commands, tasks
from random import choice

import discord, datetime, time, requests

# --------------------------------------------------------------------------------------------------------------------------------

class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'My Server Ping ({round(self.bot.latency * 1000)}ms)')

    @commands.command()
    async def oauth(self, ctx): 
        await ctx.send(f"Here is my https://discord.com/oauth2/authorize?client_id=985075081535451186&permissions=8")

    @commands.command()
    async def github(self, ctx):
        embed=discord.Embed(title="Trinix's Github", description=f"", color=0x7289da)
        embed.add_field(name="GitHub", value=f"Here is my [Github](https://github.com/UnknownToska/Trinix/)")
        await ctx.send(embed=embed)

    @commands.command(aliases=['pwg'])
    async def passgen(self, ctx):
        API = "https://www.passwordrandom.com/query?command=password"
        x = requests.get(API)
        await ctx.author.send(x.text)

def setup(bot): #Must have a setup function
    bot.add_cog(misc(bot)) # Add the class to the cog.

# --------------------------------------------------------------------------------------------------------------------------------
