# ---------------------------------------------------------------- Required Imports ----------------------------------------------------------------

from discord.ext import commands, tasks

import discord, requests

# --------------------------------------------------------------------------------------------------------------------------------

class apis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def neko(self, ctx, arg, member:discord.Member = None):
        r = requests.get(f"https://neko-love.xyz/api/v1/{arg}")
        if arg == "hug":
            embed = discord.Embed(color=0x7289da)
            if (member == ctx.author or member == None):
                embed.set_author(name=f"{ctx.author.name} Hugged Themself.")
            else:
                embed.set_author(name=f"{ctx.author.name} Hugged {member.name}.")
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)

        elif arg == "pat":
            embed = discord.Embed(color=0x7289da)
            if (member == ctx.author or member == None):
                embed.set_author(name=f"{ctx.author.name} Patted Themself.")
            else:
                embed.set_author(name=f"{ctx.author.name} Patted {member.name}.")
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)

        elif arg == "kiss":
            embed = discord.Embed(color=0x7289da)
            if (member == ctx.author or member == None):
                embed.set_author(name=f"{ctx.author.name} Kissed Themself.")
            else:
                embed.set_author(name=f"{ctx.author.name} Has Kissed {member.name}.")
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)

        elif arg == "slap":
            embed = discord.Embed(color=0x7289da)
            if (member == ctx.author or member == None):
                embed.set_author(name=f"{ctx.author.name} Slapped Themself.")
            else:
                embed.set_author(name=f"{ctx.author.name} Slapped {member.name}. OUCH")
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)

        elif arg == "punch":
            embed = discord.Embed(color=0x7289da)
            if (member == ctx.author or member == None):
                embed.set_author(name=f"{ctx.author.name} Punched Themself.")
            else:
                embed.set_author(name=f"{ctx.author.name} Punched {member.name}.")
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)

        elif arg == "smug":
            embed = discord.Embed(color=0x7289da)
            if (member == ctx.author or member == None):
                embed.set_author(name=f"{ctx.author.name} Smugged..")
            else:
                embed.set_author(name=f"{ctx.author.name} Has Smugged at {member.name}.")
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)

        elif arg == "waifu":
            embed = discord.Embed(color=0x7289da)
            if (member == ctx.author or member == None):
                embed.set_author(name=f"{ctx.author.name} Has Generated A Waifu")
            else:
                embed.set_author(name=f"{ctx.author.name} Has Generated A Waifu For {member.name}.")
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)

        elif arg == "kitsune":
            embed = discord.Embed(color=0x7289da)
            if (member == ctx.author or member == None):
                embed.set_author(name=f"{ctx.author.name} Has Generated A Kitsune")
            else:
                embed.set_author(name=f"{ctx.author.name} Has Generated A Kitsune For {member.name}.")
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)

        elif arg == "cry":
            embed = discord.Embed(color=0x7289da)
            embed.set_author(name=f"{ctx.author.name} Is crying </3 whas wrong?....")
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)
                
        elif arg == "nekolewd":
            embed = discord.Embed(color=0x7289da)
            embed.set_author(name=f"{ctx.author.name} Has Generated Nekolewd UwU")
            embed.set_image(url=(r.json()["url"]))
            await ctx.send(embed=embed)
        else: 
            embed=discord.Embed(title="[Trinix Error System]", description="[ERROR]This isn't a command.", color=0xff0000)
            await ctx.send(embed=embed)

    @commands.command()
    async def fun(self, ctx, arg):
        r = requests.get(url = f"https://api.truthordarebot.xyz/v1/{arg}")
        if arg == "truth":
            embed = discord.Embed(title="Trinix Truth", description=(r.json()["question"]), color=0x7289da)
            await ctx.send(embed=embed)

        elif arg == "dare":
            embed = discord.Embed(title="Trinix Dare", description=(r.json()["question"]), color=0x7289da)
            await ctx.send(embed=embed)

        elif arg == "wyr":
            embed = discord.Embed(title="Trinix Would You Rather", description=(r.json()["question"]), color=0x7289da)
            await ctx.send(embed=embed)

        elif arg == "nhie":
            embed = discord.Embed(title="Trinix Never Have I Ever", description=(r.json()["question"]), color=0x7289da)
            await ctx.send(embed=embed)

        elif arg == "paranoia":
            embed = discord.Embed(title="Trinix paranoia", description=(r.json()["question"]), color=0x7289da)
            await ctx.send(embed=embed)
        else: 
            embed=discord.Embed(title="[Trinix Error System]", description="[ERROR]This isn't a command.", color=0xff0000)
            await ctx.send(embed=embed)

def setup(bot): #Must have a setup function
    bot.add_cog(apis(bot)) # Add the class to the cog.
# --------------------------------------------------------------------------------------------------------------------------------
