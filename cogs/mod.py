# Please mind if the bot isnt kicking or banning any members its probably because the bot is below the members. Move Trinix role or make a bot role
# and put it above the members. 

# ---------------------------------------------------------------- Required Imports ----------------------------------------------------------------

from discord.ext import commands, tasks
import discord

# --------------------------------------------------------------------------------------------------------------------------------

class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases= ['purge','delete','clear'])
    @commands.has_permissions(administrator=True)
    async def clean(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        embed = discord.Embed(title="[Mod System] Chat Purge", description=f"{ctx.author.mention} Deleted {limit} messages.", color=0x7289da)
        embed.set_footer(text=f"{ctx.message.guild.name}", icon_url = ctx.guild.icon)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, reason = None):
        await ctx.channel.purge(limit=1)
        if reason == "None":
            await member.kick(reason = "None")
        else:
            await member.kick(reason=reason)
        embed=discord.Embed(title="Trinix Mod System", description=f"{member.mention} has been kicked from this server by {ctx.author.mention}", color=0x7289da)
        embed.add_field(name="Reason", value=f"{reason}")
        await ctx.send(embed=embed)  

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, reason = None):
        await ctx.channel.purge(limit=1)
        if reason == None:
            await member.ban(reason = "None")
        else:
            await member.ban(reason = "None")
        embed=discord.Embed(title="[Mod System] Ban Member", description=f"{member.mention} has been Banned from this server by {ctx.author.mention}", color=0x7289da)
        embed.add_field(name="Reason", value=f"{reason}")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def unban(self, ctx, id): 
        await ctx.channel.purge(limit=1)
        b = await ctx.guild.bans()
        for i in b:
            u = i.user
            if u.id == id:
                await ctx.guild.unban(u)
                embed=discord.Embed(title="Trinix Mod System", description=f"{u} has been unbanned", color=0x7289da)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def announce(self, ctx, *, message):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(title=f"{ctx.message.guild.name} Announcement!", description=message, color=0x7289da)
        embed.set_footer(text=f"{ctx.message.guild.name}", icon_url = ctx.guild.icon)
        await ctx.send(embed=embed)

def setup(bot): #Must have a setup function
    bot.add_cog(mod(bot)) # Add the class to the cog.

# --------------------------------------------------------------------------------------------------------------------------------
