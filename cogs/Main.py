#Required Imports
import discord
import random
import requests
import http
from discord.ext import commands, tasks
from random import choice, choices
from io import BytesIO

footer = "https://cdn.discordapp.com/attachments/888282878973194271/891935435859820574/default.png"

class Main(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot

    #Main Commands
    @commands.command(name='hello')
    async def hello(self, ctx):
        responses  = ['Wassup am Trinix! who are you?', 'Am smoking hold up.', 'Hello, how are you?', 'Hi', 'Wasssuup!']
        await ctx.reply(choice(responses))

    @commands.command(name='random')
    async def random(self, ctx):
        responses = ['I talk, he talk, why you middle talk?', 'You rotate the ground 4 times..', 'You go and understand the tree.', 'Dont make noise.. principle is rotating in the corridor']
        await ctx.reply(choice(responses))
    
    @commands.command(name='roast')
    async def roast(self, ctx, member:discord.Member = None):
        response = [f'{ctx.author.mention} If laughter is the best medicine, your face must be curing the world.', f'{ctx.author.mention} Youre so ugly that when you tried to enter an ugly contest the judges said, "sorry, no professionals".', f'{ctx.author.mention} Youre so ugly that when you were born they had to put dark tints on your incubator.', f'{ctx.author.mention} Youre so ugly that when you went to the haunted house you came out with a job application.', f'{ctx.author.mention} Youre so ugly, when your mom dropped you off at school she got a fine for littering.', f'{ctx.author.mention} Youre so dumb that when you heard it was chilly outside you ran and got a bowl and spoon.', f'{ctx.author.mention} I am not saying that you are stupid, just that you are constantly unlucky when you try thinking.', f'{ctx.author.mention} Youre so hairy that when you come out of the shower it is like Gorillas In The Mist.', f'{ctx.author.mention} You are so old that when you pass away, there will be a worldwide race between paleontologists to dig you up.']
        if (member == ctx.author or member == None):
            await ctx.reply(choice(response))
        else:
            responses = [f'{member.mention} If laughter is the best medicine, your face must be curing the world.', f'{member.mention} Youre so ugly that when you tried to enter an ugly contest the judges said, "sorry, no professionals".', f'{member.mention} Youre so ugly that when you were born they had to put dark tints on your incubator.', f'{member.mention} Youre so ugly that when you went to the haunted house you came out with a job application.', f'{member.mention} Youre so ugly, when your mom dropped you off at school she got a fine for littering.', f'{member.mention} Youre so dumb that when you heard it was chilly outside you ran and got a bowl and spoon.', f'{member.mention} I am not saying that you are stupid, just that you are constantly unlucky when you try thinking.', f'{member.mention} Youre so hairy that when you come out of the shower it is like Gorillas In The Mist.', f'{member.mention} You are so old that when you pass away, there will be a worldwide race between paleontologists to dig you up.']
            await ctx.send(choice(responses))

    @commands.command(name='ppsize')
    async def ppsize(self, ctx, member:discord.Member = None):
        response = [f'{ctx.author.mention} ppsize: 8=D', f'{ctx.author.mention} ppsize: 8========D', f'{ctx.author.mention} ppsize: 8=========D', f'{ctx.author.mention} ppsize: 8=================D', f'{ctx.author.mention} ppsize: 8===================D']
        if (member == ctx.author or member == None):
            await ctx.reply(choice(response))
        else:
            responses = [f'here is {member.mention} ppsize: 8=D', f'here is {member.mention} ppsize: 8========D', f'here is {member.mention} ppsize: 8=========D', f'here is {member.mention} ppsize: 8=================D', f'here is {member.mention} ppsize: 8===================D']
            await ctx.send(choice(responses))

    @commands.command(name='coinflip', aliases=["flip", "coin"])
    async def coinflip(self, ctx):
        coinside = ["Heads", "Tails"]
        coin = f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinside)}**!"
        embed=discord.Embed(title="Trinix Bot", color = discord.Color.blurple())
        embed.set_footer(text="Trinix made by: Maxim", icon_url=footer)
        embed.add_field(name="Results", value=coin, inline=False)
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(name='rate')
    async def rate(self, ctx, *, member:discord.Member = None):
        rate = random.uniform(0, 10)
        rateSelfResponse = f"I'd rate {ctx.author.mention} a **{round(rate)} / 10**"
        if (member == ctx.author or member == None ):
            embed=discord.Embed(title="Trinix Rate", description="", color = discord.Color.blurple())
            embed.add_field(name="Results", value=rateSelfResponse, inline=False)
            embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
            await ctx.reply(embed=embed, mention_author=False)
        else:
            ratea = f"I'd rate {member.mention} a **{round(rate)} / 10**"
            embed=discord.Embed(title="Trinix Rate", description="", color = discord.Color.blurple())
            embed.add_field(name="Results", value=ratea, inline=False)
            embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
            await ctx.reply(embed=embed, mention_author=False)

    @commands.command(name='simprate', aliases=["sr"])
    async def simprate(self, ctx, *, member:discord.Member = None):
        rate = random.uniform(0, 100)
        simprateSelfResponse = f" {ctx.author.mention} is **{round(rate)} %** a simp"
        if (member == ctx.author or member == None ):
            embed=discord.Embed(title="Trinix Simp Rate", description="", color = discord.Color.blurple())
            embed.add_field(name="Results", value=simprateSelfResponse, inline=False)
            embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
            await ctx.reply(embed=embed, mention_author=False)
        else:
            ratea = f"{member.mention} is **{round(rate)} %** a simp"
            embed=discord.Embed(title="Trinix Rate", description="", color = discord.Color.blurple())
            embed.add_field(name="Results", value=ratea, inline=False)
            embed.set_footer(text="Trinix Made by: Maxim", icon_url = footer)
            await ctx.reply(embed=embed, mention_author=False) 
    
def setup(bot): #Must have a setup function
    bot.add_cog(Main(bot)) # Add the class to the cog.
