from discord.ext import commands
from discord import Option

import discord, requests

endpoints = requests.get(f"https://nekos.best/api/v2/endpoints").json()
actions = list(endpoints.keys())[:25]

class apis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Nekos Commands")
    async def neko(self, ctx, action: Option(str, "Choose a action!", choices=actions), member:discord.Member = None):
        r = requests.get(f"https://nekos.best/api/v2/{action}")
        embed = discord.Embed(color=0x7289da)
        if (member == ctx.author or member == None):
            embed.set_author(name=f"{ctx.author.name} has used {action}")
        else:
            embed.set_author(name=f"{ctx.author.name} Has used {action} on {member.name}")
        embed.set_image(url=(r.json()["results"][0]["url"]))
        await ctx.respond(embed=embed)

    @commands.slash_command(description="Some fun commands")
    async def fun(self, ctx, arg: Option(str, "Fun commands", choices=["truth", "dare", "wyr", "nhie", "paranoia"])):
        r = requests.get(url = f"https://api.truthordarebot.xyz/v1/{arg}")
        if arg == "truth":
            embed = discord.Embed(title="Trinix Truth", description=(r.json()["question"]), color=0x7289da)
            await ctx.respond(embed=embed)

        elif arg == "dare":
            embed = discord.Embed(title="Trinix Dare", description=(r.json()["question"]), color=0x7289da)
            await ctx.respond(embed=embed)

        elif arg == "wyr":
            embed = discord.Embed(title="Trinix Would You Rather", description=(r.json()["question"]), color=0x7289da)
            await ctx.respond(embed=embed)

        elif arg == "nhie":
            embed = discord.Embed(title="Trinix Never Have I Ever", description=(r.json()["question"]), color=0x7289da)
            await ctx.respond(embed=embed)

        elif arg == "paranoia":
            embed = discord.Embed(title="Trinix paranoia", description=(r.json()["question"]), color=0x7289da)
            await ctx.respond(embed=embed)
        else: 
            embed=discord.Embed(title="[Trinix Error System]", description="[ERROR]This isn't a command.", color=0xff0000)
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(apis(bot))
