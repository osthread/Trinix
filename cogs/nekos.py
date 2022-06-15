# ---------------------------------------------------------------- Required Imports ----------------------------------------------------------------
from discord.ext import commands, tasks
from random import choice

import discord, random, requests

# --------------------------------------------------------------------------------------------------------------------------------

class nekos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# ---------------------------------------------------------------- Neko Commands ----------------------------------------------------------------

    @commands.command()
    async def n(self, ctx, arg, member:discord.Member = None):

        r = requests.get(f"https://neko-love.xyz/api/v1/{arg}")

        if arg == "hug":
            try:
                if (member == ctx.author or member == None):
                    embed = discord.Embed(color=0x7289da)
                    embed.set_author(name=f"{ctx.author.name} Hugged Themself.")
                    embed.set_image(url=(r.json()["url"]))
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(color=0x7289da)
                    embed.set_author(name=f"{ctx.author.name} Hugged {member.name}.")
                    embed.set_image(url=(r.json()["url"]))
                    await ctx.send(embed=embed)
            except:
                print("[NEKO ERROR!]")

        elif arg == "pat":
            try:
                if (member == ctx.author or member == None):
                    embed = discord.Embed(title=f"{ctx.author.name} Patted Themself.", color=0x7289da)
                    embed.set_image(url=(r.json()["url"]))
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title=f"{ctx.author.name} Patted {member.name}.", color=0x7289da)
                    embed.set_image(url=(r.json()["url"]))
                    await ctx.send(embed=embed)
            except:
                print("[NEKO ERROR!]")

        elif arg == "kiss":
            try:
                if (member == ctx.author or member == None):
                    embed = discord.Embed(title=f"{ctx.author.name} Kissed Themself", color=0x7289da)
                    embed.set_image(url=(r.json()["url"]))
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title=f"Kissed {member.name}", color=0x7289da)
                    embed.set_image(url=(r.json()["url"]))
                    await ctx.send(embed=embed)
            except:
                print("[NEKO ERROR!]")

        elif arg == "slap":
            try:
                if (member == ctx.author or member == None):
                    embed = discord.Embed(title=f"{ctx.author.name} Slapped Themself.", color=0x7289da)
                    embed.set_image(url=(r.json()["url"]))
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title=f"{ctx.author.name} Slapped {member.name}.", color=0x7289da)
                    embed.set_image(url=(r.json()["url"]))
                    await ctx.send(embed=embed)
            except:
                print("[NEKO ERROR!]")

        elif arg == "punch":
            try:
                if (member == ctx.author or member == None):
                    embed = discord.Embed(title=f"{ctx.author.name} Punched Themself.", color=0x7289da)
                    embed.set_image(url=(r.json()["url"]))
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title=f"{ctx.author.name} Punched {member.name}.", color=0x7289da)
                    embed.set_image(url=(r.json()["url"]))
                    await ctx.send(embed=embed)
            except:
                print("[NEKO ERROR!]")

        elif arg == "smug":
            try:
                embed = discord.Embed(title=f"{ctx.author.name} Smugged", color=0x7289da)
                embed.set_image(url=(r.json()["url"]))
                await ctx.send(embed=embed)
            except:
                print("[NEKO ERROR!]")

        elif arg == "waifu":
            try:
                embed = discord.Embed(title=f"{ctx.author.name} Generated A Waifu!", color=0x7289da)
                embed.set_image(url=(r.json()["url"]))
                await ctx.send(embed=embed)
            except:
                print("[NEKO ERROR!]")

        elif arg == "kitsune":
            try:
                embed = discord.Embed(title=f"{ctx.author.name} Generated Kitsune!", color=0x7289da)
                embed.set_image(url=(r.json()["url"]))
                await ctx.send(embed=embed)
            except:
                print("[NEKO ERROR!]")

        elif arg == "cry":
            try:
                embed = discord.Embed(title=f"{ctx.author.name} Is Crying...", color=0x7289da)
                embed.set_image(url=(r.json()["url"]))
                await ctx.send(embed=embed)
            except:
                print("[NEKO ERROR!]")
                
        elif arg == "nekolewd":
            try:
                embed = discord.Embed(title=f"{ctx.author.name} Generated Nekolewd!", color=0x7289da)
                embed.set_image(url=(r.json()["url"]))
                await ctx.send(embed=embed)
            except:
                print("[NEKO ERROR!]")

# --------------------------------------------------------------------------------------------------------------------------------

def setup(bot): #Must have a setup function
    bot.add_cog(nekos(bot)) # Add the class to the cog.