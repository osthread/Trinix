# ---------------------------------------------------------------- Required Imports ----------------------------------------------------------------
from discord.ext import commands, tasks

import discord, datetime, os, requests

# --------------------------------------------------------------------------------------------------------------------------------

class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# ---------------------------------------------------------------- Admin Commands ----------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clean(self, ctx, limit: int):
        await ctx.channel.purge(limit=1)
        await ctx.channel.purge(limit=limit)
        embed=discord.Embed(title="Trinix Mod System", description=f'{ctx.author.mention} Has Purged {limit} Messages!', color=0x7289da)
        await ctx.respond(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member, reason):
        if reason == None:
            await ctx.channel.purge(limit=1)
            await member.kick(reason="None")
            embed=discord.Embed(title="Trinix Mod System", description=f"{member.mention} has been kicked from this server", color=0x7289da)
            await ctx.respond(embed=embed)
        else:
            await ctx.channel.purge(limit=1)
            await member.kick(reason=reason)
            embed=discord.Embed(title="Trinix Mod System", description=f"{member.mention} has been kicked from this server", color=0x7289da)
            await ctx.respond(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, reason):
        if reason == None:
            await ctx.channel.purge(limit=1)
            await member.ban(reason = "None")
            message = f'**{member.mention} has been banned from this server**'
            embed=discord.Embed(title="Trinix Mod System", description=message, color=0x7289da)
            await ctx.respond(embed=embed)
        else:
            await ctx.channel.purge(limit=1)
            await member.kick(reason=reason)
            embed=discord.Embed(title="Trinix Mod System", description=f"{member.mention} has been kicked from this server", color=0x7289da)
            await ctx.respond(embed=embed)

    @commands.command()#Unban by Panda <3
    @commands.has_permissions(administrator = True)
    async def unban(self, ctx, id): 
        await ctx.channel.purge(limit=1)
        b = await ctx.guild.bans()
        for i in b:
            u = i.user
            if u.id == id:
                await ctx.guild.unban(u)
                embed=discord.Embed(title="Trinix Mod System", description=f"{u} has been unbanned", color=0x7289da)
                await ctx.respond(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def announce(self, ctx, message):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(title=f"Announcements", description=message, color=0x7289da)
        await ctx.respond(embed=embed)

# --------------------------------------------------------------------------------------------------------------------------------

def setup(bot): # Must have a setup function
        bot.add_cog(mod(bot)) # Add the class to the cog.