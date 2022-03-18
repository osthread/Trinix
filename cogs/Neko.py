#3/17/2020 I have updated neko commads
#Required Imports
from random import choice
from discord.ext import commands, tasks

import random
import discord
import requests

class Neko(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def neko(self, ctx, endpoint, member:discord.Member = None):
                r = requests.get("https://neko-love.xyz/api/v1/" + endpoint)
                if (member == ctx.author or member == None):
                    some = f"{ctx.author.mention} Has {endpoint}ed themself"
                    embed = discord.Embed(title="Trinix Bot")
                    embed.add_field(name="Look!", value=some, inline=False)
                    embed.set_image(url=(r.json()["url"]))
                    embed.color = discord.Color.blurple()
                    await ctx.send(embed=embed)
                else:
                    some1 = f"{ctx.author.mention} Has {endpoint}ed {member.mention}"
                    embed = discord.Embed(title="Trinix Bot")
                    embed.add_field(name="Look!", value=some, inline=False)
                    embed.set_image(url=(r.json()["url"]))
                    embed.color = discord.Color.blurple()
                    await ctx.send(embed=embed)

def setup(bot): #Must have a setup function
    bot.add_cog(Neko(bot)) # Add the class to the cog.
