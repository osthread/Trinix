# ---------------------------------------------------------------- Required Imports ----------------------------------------------------------------

from discord.ext import commands, tasks
from random import choice, choices

import discord, random, requests

# --------------------------------------------------------------------------------------------------------------------------------

class main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        responses  = ['Wassup am Trinix! who are you?', 'Am smoking hold up.', 'Hello, how are you?', 'Hi', 'Wasssuup!']
        await ctx.send(choice(responses))

    @commands.command()
    async def random(self, ctx):
        responses = ['I talk, he talk, why you middle talk?', 'You rotate the ground 4 times..', 'You go and understand the tree.', 'Dont make noise.. principle is rotating in the corridor']
        await ctx.send(choice(responses))

    @commands.command()
    async def roast(self, ctx, member:discord.Member = None):
        response = [f'{ctx.author.mention} If laughter is the best medicine, your face must be curing the world.', f'{ctx.author.mention} Youre so ugly that when you tried to enter an ugly contest the judges said, "sorry, no professionals".', f'{ctx.author.mention} Youre so ugly that when you were born they had to put dark tints on your incubator.', f'{ctx.author.mention} Youre so ugly that when you went to the haunted house you came out with a job application.', f'{ctx.author.mention} Youre so ugly, when your mom dropped you off at school she got a fine for littering.', f'{ctx.author.mention} Youre so dumb that when you heard it was chilly outside you ran and got a bowl and spoon.', f'{ctx.author.mention} I am not saying that you are stupid, just that you are constantly unlucky when you try thinking.', f'{ctx.author.mention} Youre so hairy that when you come out of the shower it is like Gorillas In The Mist.', f'{ctx.author.mention} You are so old that when you pass away, there will be a worldwide race between paleontologists to dig you up.']
        if (member == ctx.author or member == None):
            await ctx.send(choice(response))
        else:
            responses = [f'{member.mention} If laughter is the best medicine, your face must be curing the world.', f'{member.mention} Youre so ugly that when you tried to enter an ugly contest the judges said, "sorry, no professionals".', f'{member.mention} Youre so ugly that when you were born they had to put dark tints on your incubator.', f'{member.mention} Youre so ugly that when you went to the haunted house you came out with a job application.', f'{member.mention} Youre so ugly, when your mom dropped you off at school she got a fine for littering.', f'{member.mention} Youre so dumb that when you heard it was chilly outside you ran and got a bowl and spoon.', f'{member.mention} I am not saying that you are stupid, just that you are constantly unlucky when you try thinking.', f'{member.mention} Youre so hairy that when you come out of the shower it is like Gorillas In The Mist.', f'{member.mention} You are so old that when you pass away, there will be a worldwide race between paleontologists to dig you up.']
            await ctx.send(choice(responses))

    @commands.command()
    async def ppsize(self, ctx, member:discord.Member = None):
        response = [f'{ctx.author.mention} ppsize: 8=D', f'{ctx.author.mention} ppsize: 8========D', f'{ctx.author.mention} ppsize: 8=========D', f'{ctx.author.mention} ppsize: 8=================D', f'{ctx.author.mention} ppsize: 8===================D']
        if (member == ctx.author or member == None):
            await ctx.send(choice(response))
        else:
            responses = [f'here is {member.mention} ppsize: 8=D', f'here is {member.mention} ppsize: 8========D', f'here is {member.mention} ppsize: 8=========D', f'here is {member.mention} ppsize: 8=================D', f'here is {member.mention} ppsize: 8===================D']
            await ctx.send(choice(responses))

    @commands.command()
    async def coinflip(self, ctx):
        coinside = ['Heads', 'Tails']
        random = choice(coinside)
        embed=discord.Embed(title=f"**{ctx.author.mention}** flipped a coin and got **{random}**!", color=0x7289da)
        await ctx.send(embed=embed)

    @commands.command()
    async def rate(self, ctx, *, member:discord.Member = None):
        rate = random.uniform(0, 10)
        if (member == ctx.author or member == None ):
            embed=discord.Embed(title="Trinix Rate", description=f"I'd rate {ctx.author.mention} a **{round(rate)} / 10**", color=0x7289da)
        else:
            embed=discord.Embed(title="Trinix Rate", description=f"I'd rate {member.mention} a **{round(rate)} / 10**", color=0x7289da)
        await ctx.send(embed=embed)

    @commands.command()
    async def simprate(self, ctx, *, member:discord.Member = None):
        rate = random.uniform(0, 100)
        if (member == ctx.author or member == None ):
            embed=discord.Embed(title="Trinix Simp Rate", description=f" {ctx.author.mention} is **{round(rate)} %** a simp", color=0x7289da)
        else:
            embed=discord.Embed(title="Trinix Simp Rate", description=f"{member.mention} is **{round(rate)} %** a simp", color=0x7289da)
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
    bot.add_cog(main(bot)) # Add the class to the cog.

# --------------------------------------------------------------------------------------------------------------------------------
