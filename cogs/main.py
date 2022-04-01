#Required Imports
from discord.ext import commands, tasks
from random import choice, choices
from io import BytesIO

import discord, random, requests, http

#API
api = 'https://api.truthordarebot.xyz/v1/'

class main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Main Commands
    @commands.command()
    async def hello(self, ctx):
        responses  = ['Wassup am Trinix! who are you?', 'Am smoking hold up.', 'Hello, how are you?', 'Hi', 'Wasssuup!']
        await ctx.reply(choice(responses))

    @commands.command()
    async def random(self, ctx):
        responses = ['I talk, he talk, why you middle talk?', 'You rotate the ground 4 times..', 'You go and understand the tree.', 'Dont make noise.. principle is rotating in the corridor']
        await ctx.reply(choice(responses))

    @commands.command()
    async def roast(self, ctx, member:discord.Member = None):
        response = [f'{ctx.author.mention} If laughter is the best medicine, your face must be curing the world.', f'{ctx.author.mention} Youre so ugly that when you tried to enter an ugly contest the judges said, "sorry, no professionals".', f'{ctx.author.mention} Youre so ugly that when you were born they had to put dark tints on your incubator.', f'{ctx.author.mention} Youre so ugly that when you went to the haunted house you came out with a job application.', f'{ctx.author.mention} Youre so ugly, when your mom dropped you off at school she got a fine for littering.', f'{ctx.author.mention} Youre so dumb that when you heard it was chilly outside you ran and got a bowl and spoon.', f'{ctx.author.mention} I am not saying that you are stupid, just that you are constantly unlucky when you try thinking.', f'{ctx.author.mention} Youre so hairy that when you come out of the shower it is like Gorillas In The Mist.', f'{ctx.author.mention} You are so old that when you pass away, there will be a worldwide race between paleontologists to dig you up.']
        if (member == ctx.author or member == None):
            await ctx.reply(choice(response))
        else:
            responses = [f'{member.mention} If laughter is the best medicine, your face must be curing the world.', f'{member.mention} Youre so ugly that when you tried to enter an ugly contest the judges said, "sorry, no professionals".', f'{member.mention} Youre so ugly that when you were born they had to put dark tints on your incubator.', f'{member.mention} Youre so ugly that when you went to the haunted house you came out with a job application.', f'{member.mention} Youre so ugly, when your mom dropped you off at school she got a fine for littering.', f'{member.mention} Youre so dumb that when you heard it was chilly outside you ran and got a bowl and spoon.', f'{member.mention} I am not saying that you are stupid, just that you are constantly unlucky when you try thinking.', f'{member.mention} Youre so hairy that when you come out of the shower it is like Gorillas In The Mist.', f'{member.mention} You are so old that when you pass away, there will be a worldwide race between paleontologists to dig you up.']
            await ctx.reply(choice(responses))

    @commands.command()
    async def ppsize(self, ctx, member:discord.Member = None):
        response = [f'{ctx.author.mention} ppsize: 8=D', f'{ctx.author.mention} ppsize: 8========D', f'{ctx.author.mention} ppsize: 8=========D', f'{ctx.author.mention} ppsize: 8=================D', f'{ctx.author.mention} ppsize: 8===================D']
        if (member == ctx.author or member == None):
            await ctx.reply(choice(response))
        else:
            responses = [f'here is {member.mention} ppsize: 8=D', f'here is {member.mention} ppsize: 8========D', f'here is {member.mention} ppsize: 8=========D', f'here is {member.mention} ppsize: 8=================D', f'here is {member.mention} ppsize: 8===================D']
            await ctx.reply(choice(responses))

    @commands.command(aliases=["flip", "coin"])
    async def coinflip(self, ctx):
        coinside = ["Heads", "Tails"]
        coin = f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinside)}**!"
        embed=discord.Embed(title="Trinix Bot", color = discord.Color.blurple())
        embed.set_ctx.guild.icon_url(text="Trinix", icon_url=ctx.guild.icon_url)
        embed.add_field(name="Results", value=coin, inline=False)
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def rate(self, ctx, *, member:discord.Member = None):
        rate = random.uniform(0, 10)
        rateSelfResponse = f"I'd rate {ctx.author.mention} a **{round(rate)} / 10**"
        if (member == ctx.author or member == None ):
            embed=discord.Embed(title="Trinix Rate", description="", color = discord.Color.blurple())
            embed.add_field(name="Results", value=rateSelfResponse, inline=False)
            embed.set_ctx.guild.icon_url(text="Trinix", icon_url = ctx.guild.icon_url)
            await ctx.reply(embed=embed, mention_author=False)
        else:
            ratea = f"I'd rate {member.mention} a **{round(rate)} / 10**"
            embed=discord.Embed(title="Trinix Rate", description="", color = discord.Color.blurple())
            embed.add_field(name="Results", value=ratea, inline=False)
            embed.set_ctx.guild.icon_url(text="Trinix", icon_url = ctx.guild.icon_url)
            await ctx.reply(embed=embed, mention_author=False)

    @commands.command(aliases=["sr"])
    async def simprate(self, ctx, *, member:discord.Member = None):
        rate = random.uniform(0, 100)
        simprateSelfResponse = f" {ctx.author.mention} is **{round(rate)} %** a simp"
        if (member == ctx.author or member == None ):
            embed=discord.Embed(title="Trinix Simp Rate", description="", color = discord.Color.blurple())
            embed.add_field(name="Results", value=simprateSelfResponse, inline=False)
            embed.set_ctx.guild.icon_url(text="Trinix", icon_url = ctx.guild.icon_url)
            await ctx.reply(embed=embed, mention_author=False)
        else:
            ratea = f"{member.mention} is **{round(rate)} %** a simp"
            embed=discord.Embed(title="Trinix Rate", description="", color = discord.Color.blurple())
            embed.add_field(name="Results", value=ratea, inline=False)
            embed.set_ctx.guild.icon_url(text="Trinix", icon_url = ctx.guild.icon_url)
            await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def geolocate(self, ctx, ip):
        r = requests.get( url = f'https://ipinfo.io/{ip}/geo')
        embed = discord.Embed(title="Trinix Geo Location")
        embed.add_field(name="Ip", value=(r.json()["ip"]), inline=False)
        embed.add_field(name="City", value=(r.json()["city"]), inline=False)
        embed.add_field(name="Region", value=(r.json()["region"]), inline=False)
        embed.add_field(name="Country", value=(r.json()["country"]), inline=False)
        embed.add_field(name="Location", value=(r.json()["loc"]), inline=False)
        embed.add_field(name="Org", value=(r.json()["org"]), inline=False)
        embed.add_field(name="Timezone", value=(r.json()["timezone"]), inline=False)
        embed.set_ctx.guild.icon_url(text="Trinix", icon_url = ctx.guild.icon_url)
        embed.color = discord.Color.blurple()
        await ctx.send(embed=embed)

    @commands.command()
    async def truth(self, ctx):
        endpoint = 'truth'
        r = requests.get(api + endpoint)
        embed = discord.Embed(title="Trinix Truth Gen")
        embed.add_field(name="Truth Question", value=(r.json()["question"]), inline=False)
        embed.set_ctx.guild.icon_url(text="Trinix", icon_url = ctx.guild.icon_url)
        embed.color = discord.Color.blurple()
        await ctx.send(embed=embed)

    @commands.command()
    async def truth(self, ctx):
        endpoint = 'dare'
        r = requests.get(api + endpoint)
        embed = discord.Embed(title="Trinix Dare Gen")
        embed.add_field(name="Dare", value=(r.json()["question"]), inline=False)
        embed.set_ctx.guild.icon_url(text="Trinix", icon_url = ctx.guild.icon_url)
        embed.color = discord.Color.blurple()
        await ctx.send(embed=embed)

    @commands.command()
    async def wyr(self, ctx):
        endpoint = 'wyr'
        r = requests.get(api + endpoint)
        embed = discord.Embed(title="Trinix Would You Rather Gen")
        embed.add_field(name="Would You Rather Question", value=(r.json()["question"]), inline=False)
        embed.set_ctx.guild.icon_url(text="Trinix", icon_url = ctx.guild.icon_url)
        embed.color = discord.Color.blurple()
        await ctx.send(embed=embed)

    @commands.command()
    async def nhie(self, ctx):
        endpoint = 'nhie'
        r = requests.get(api + endpoint)
        embed = discord.Embed(title="Trinix Never Have I Ever Gen")
        embed.add_field(name="Never Have I Ever Question", value=(r.json()["question"]), inline=False)
        embed.set_ctx.guild.icon_url(text="Trinix", icon_url = ctx.guild.icon_url)
        embed.color = discord.Color.blurple()
        await ctx.send(embed=embed)

    @commands.command()
    async def paranoia(self, ctx):
        endpoint = 'paranoia'
        r = requests.get(api + endpoint)
        embed = discord.Embed(title="Trinix Paranoia Gen")
        embed.add_field(name="Paranoia Question", value=(r.json()["question"]), inline=False)
        embed.set_ctx.guild.icon_url(text="Trinix", icon_url = ctx.guild.icon_url)
        embed.color = discord.Color.blurple()
        await ctx.send(embed=embed)

def setup(bot): #Must have a setup function
    bot.add_cog(main(bot)) # Add the class to the cog.
