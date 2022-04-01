#Required Imports
from discord.ext import commands, tasks
from random import choice

import discord, random, requests


api = 'https://neko-love.xyz/api/v1/'

class nekos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hug(self, ctx, member:discord.Member = None):
        endpoint = 'hug'
        r = requests.get(api + endpoint)
        if (member == ctx.author or member == None):
            some = f"{ctx.author.mention} Has hugged themself"
            embed = discord.Embed(title="Trinix", description=some, color = discord.Color.blurple())
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)
        else:
            some1 = f"{ctx.author.mention} Has hugged {member.mention}"
            embed = discord.Embed(title="Trinix", description=some1, color = discord.Color.blurple())
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)

    @commands.command()
    async def pat(self, ctx, member:discord.Member = None):
        endpoint = 'pat'
        r = requests.get(api + endpoint)
        if (member == ctx.author or member == None):
            some = f"{ctx.author.mention} Has Patted themself"
            embed = discord.Embed(title="Trinix", description=some, color = discord.Color.blurple())
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)
        else:
            some1 = f"{ctx.author.mention} Has Patted {member.mention}"
            embed = discord.Embed(title="Trinix", description=some1, color = discord.Color.blurple())
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx, member:discord.Member = None):
        endpoint = 'kiss'
        r = requests.get(api + endpoint)
        if (member == ctx.author or member == None):
            some = f"{ctx.author.mention} Has Kissed themself"
            embed = discord.Embed(title="Trinix", description=some, color = discord.Color.blurple())
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)
        else:
            some1 = f"{ctx.author.mention} Has Kissed {member.mention}"
            embed = discord.Embed(title="Trinix", description=some1, color = discord.Color.blurple())
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx, member:discord.Member = None):
        endpoint = 'slap'
        r = requests.get(api + endpoint)
        if (member == ctx.author or member == None):
            some = f"{ctx.author.mention} Has Slapped themself"
            embed = discord.Embed(title="Trinix", description=some, color = discord.Color.blurple())
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)
        else:
            some1 = f"{ctx.author.mention} Has Slapped {member.mention}"
            embed = discord.Embed(title="Trinix", description=some1, color = discord.Color.blurple())
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)

    @commands.command()
    async def punch(self, ctx, member:discord.Member = None):
        endpoint = 'punch'
        r = requests.get(api + endpoint)
        if (member == ctx.author or member == None):
            some = f"{ctx.author.mention} Has Punched themself"
            embed = discord.Embed(title="Trinix", description=some, color = discord.Color.blurple())
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)
        else:
            some1 = f"{ctx.author.mention} Has Punched {member.mention}"
            embed = discord.Embed(title="Trinix", description=some1, color = discord.Color.blurple())
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)

    @commands.command()
    async def smug(self, ctx, member:discord.Member = None):
        endpoint = 'smug'
        r = requests.get(api + endpoint)
        if (member == ctx.author or member == None):
            some = f"{ctx.author.mention} Has smugged"
            embed = discord.Embed(title="Trinix", description=some, color = discord.Color.blurple())
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)

    @commands.command()
    async def waifu(self, ctx, member:discord.Member = None):
        endpoint = 'waifu'
        r = requests.get(api + endpoint)
        if (member == ctx.author or member == None):
            some = f"{ctx.author.mention} Has Generated A Waifu!"
            embed = discord.Embed(title="Trinix", description=some, color = discord.Color.blurple())
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)

    @commands.command()
    async def kitsune(self, ctx, member:discord.Member = None):
        endpoint = 'kitsune'
        r = requests.get(api + endpoint)
        if (member == ctx.author or member == None):
            some = f"{ctx.author.mention} Has Generated Kitsune!"
            embed = discord.Embed(title="Trinix", description=some, color = discord.Color.blurple())
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)

    @commands.command()
    async def cry(self, ctx, member:discord.Member = None):
        endpoint = 'cry'
        r = requests.get(api + endpoint)
        if (member == ctx.author or member == None):
            some = f"{ctx.author.mention} is crying..."
            embed = discord.Embed(title="Trinix", description=some, color = discord.Color.blurple())
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)

    @commands.command()
    async def nekolewd(self, ctx, member:discord.Member = None):
        endpoint = 'nekolewd'
        r = requests.get(api + endpoint)
        if (member == ctx.author or member == None):
            some = f"{ctx.author.mention} Has Generated Nekolewd!"
            embed = discord.Embed(title="Trinix", description=some, color = discord.Color.blurple())
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)

def setup(bot): #Must have a setup function
    bot.add_cog(nekos(bot)) # Add the class to the cog.
