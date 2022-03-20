#Required Imports
from discord import message
from discord.ext import commands, tasks

import discord, datetime

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Admin Commands
    @commands.command(aliases= ['purge','delete','clean'])
    @commands.has_permissions(administrator=True)
    async def clean(self, ctx, limit: int):
            await ctx.channel.purge(limit=limit)
            message = f'{limit} messages have been purged by {ctx.message.author.mention}'
            embed=discord.Embed(title="Trinix Mod System", description=message, color=0x7289da)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members = True)# This makes it where only admins can use this command
    async def kick(self, ctx, member: discord.Member, *, why=None):
        await member.kick(reason=why)
        message = f"**{member} has been kicked from this server by {ctx.message.author.mentionr}**"
        embed=discord.Embed(title="Trinix Mod System", description=message, color=0x7289da)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)
        message = f'**{member} has been banned from this server by {ctx.message.author.mention}**'
        embed=discord.Embed(title="Trinix Mod System", description=message, color=0x7289da)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator = True)# This makes it where only admins can use this command
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def announce(self, ctx, *, message):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(title=f"{ctx.message.guild.name} Announcements", description=message, color=0x7289da)
        embed.set_footer(text=f"{ctx.message.guild.name}", icon_url = ctx.guild.icon_url)
        await ctx.send(embed=embed)

def setup(bot): # Must have a setup function
        bot.add_cog(Mod(bot)) # Add the class to the cog.
