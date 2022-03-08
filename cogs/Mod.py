#Required Imports
from discord import message
from discord.ext import commands, tasks

import discord
import datetime

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Admin Commands
    @commands.command(name='clear', aliases= ['purge','delete'])
    @commands.has_permissions(administrator=True)#This makes it where only admins can use this command
    async def clear(self, ctx, amount=1000):
        channel = ctx.message.channel
        messages = []
        async for message in channel.history(limit=amount + 1):
                  messages.append(message)

        await channel.delete_messages(messages)
        message = f'{amount} messages have been purged by {ctx.message.author.mention}'
        embed=discord.Embed(title="Trinix Mod System", description=message, color=0xff0000)
        await ctx.send(embed=embed)

    @commands.command(name='kick')
    @commands.has_permissions(kick_members = True)#This makes it where only admins can use this command
    async def kick(self, ctx, member: discord.Member, *, why=None):
        await member.kick(reason=why)
        message = f"**{member} has been kicked from this server by {ctx.author}**"
        embed=discord.Embed(title="Trinix Mod System", description=message, color=0xff0000)
        await ctx.send(embed=embed)

    @commands.command(name='ban')
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)
        message = f'**{member} has been banned from this server by {ctx.author}**'
        embed=discord.Embed(title="Trinix Mod System", description=message, color=0xff0000)
        await ctx.send(embed=embed)

    @commands.command(name='unban')
    @commands.has_permissions(administrator = True)#This makes it where only admins can use this command
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

def setup(bot): #Must have a setup function
        bot.add_cog(Mod(bot)) # Add the class to the cog.
