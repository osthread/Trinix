# ---------------------------------------------------------------- Required Imports ----------------------------------------------------------------

import discord, json
from discord.ext import commands, tasks

# --------------------------------------------------------------------------------------------------------------------------------

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, arg, cmd=None):

        if arg == "cmd":
            embed = discord.Embed(color=0x7289da)
            embed.title = "[Trinix Help Dashboard]"
            if ctx.message.author.guild_permissions.administrator:
                embed.add_field(name=":shield: **Admin Commands**", value="Command: `.help admin`", inline=False)
            embed.add_field(name=":loud_sound: **Music Commands**", value="Command: `.help music`", inline=False)
            embed.add_field(name=":cyclone: **Misc Commands**", value="Command: `.help misc`", inline=False)
            embed.add_field(name=":sparkles: **Neko Commands**", value="Command: `.help neko`", inline=False)
            embed.add_field(name=":tada: **Fun Commands**", value="Command: `.help fun`", inline=False)
            embed.set_footer(text="Trinix", icon_url = ctx.guild.icon)
            await ctx.send(embed=embed)

        elif arg == "fun":
            embed = discord.Embed(color=0x7289da)
            embed.title = "[Trinix Fun Help Dashboard]"
            embed.add_field(name="**Random Hello Message**", value="Command: `.hello`", inline=False)
            embed.add_field(name="**Random Message**", value="Command: `.random`", inline=False)
            embed.add_field(name="**Roasting Members**", value="Command: `.roast <@user>`", inline=False)
            embed.add_field(name="**Random Ppsize**", value="Command: `.ppsize <@user>`", inline=False)
            embed.add_field(name="**Heads Or Tails**", value="Command: `.coinflip`", inline=False)
            embed.add_field(name="**Rating Members Looks**", value="Command: `.rate <@user>`", inline=False)
            embed.add_field(name="**Simp Rating Members**", value="Command: `.simprate <@user>`", inline=False)
            embed.add_field(name="**Get Truth**", value="Command: `.fun truth`", inline=False)
            embed.add_field(name="**Get Dare**", value="Command: `.fun dare`", inline=False)
            embed.add_field(name="**Get Would You Ratherr**", value="Command: `.fun wyr`", inline=False)
            embed.add_field(name="**Get Never Have I Ever**", value="Command: `.fun nhie`", inline=False)
            embed.add_field(name="**Get Paranoia Question**", value="Command: `.fun nhie`", inline=False)
            embed.set_footer(text="Trinix", icon_url = ctx.guild.icon)
            await ctx.send(embed=embed)

        elif arg == "music":
            embed = discord.Embed(color=0x7289da)
            embed.title = "[Trinix Music Help Dashboard] Updating Commands"
            embed.add_field(name="**Playing Music**", value="Command: `.play <name.link>`", inline=False)
            embed.add_field(name="**Bot leave**", value="Command: `.stop`", inline=False)
            embed.set_footer(text="Trinix", icon_url = ctx.guild.icon)
            await ctx.send(embed=embed)

        elif arg == "misc":
            embed = discord.Embed(color=0x7289da)
            embed.title = "[Trinix Misc Help Dashboard]"
            embed.add_field(name="how Bot Uptime", value="Command: `.ping`", inline=False)
            embed.add_field(name="Show Bot Ping", value="Command: `.ms`", inline=False)
            embed.add_field(name="Trinix Oauth", value="Command: `.oauth`", inline=False)
            embed.set_footer(text="Trinix", icon_url = ctx.guild.icon)
            await ctx.send(embed=embed)

        elif arg == "neko":
            embed = discord.Embed(color=0x7289da)
            embed.title = "[Trinix Neko Help Dashboard]"
            embed.add_field(name="**Hugging Members**", value="Command: `.n hug <@user>`", inline=False)
            embed.add_field(name="**Patting Members**", value="Command: `.n pat <@user>`", inline=False)
            embed.add_field(name="**Kissing Members**", value="Command: `.n kiss <@user>`", inline=False)
            embed.add_field(name="**Slapping Members**", value="Command: `.n slap <@user>`", inline=False)
            embed.add_field(name="**Punching Members**", value="Command: `.n punch <@user>`", inline=False)
            embed.add_field(name="**Random Nekolewd**", value="Command: `.n nekolewd`", inline=False)
            embed.add_field(name="**Random Kitsune**", value="Command: `.n kitsune`", inline=False)
            embed.add_field(name="**Random Waifu**", value="Command: `.n waifu`", inline=False)
            embed.add_field(name="**Random Neko**", value="Command: `.n neko`", inline=False)
            embed.add_field(name="**Self Crying**", value="Command: `.n cry`", inline=False)
            embed.add_field(name="**Self Smug**", value="Command: `.n smug`", inline=False)
            embed.set_footer(text="Trinix", icon_url = ctx.guild.icon)
            await ctx.send(embed=embed)

        elif arg == "admin":
            if ctx.message.author.guild_permissions.administrator:
                embed = discord.Embed(color=0x7289da)
                embed.title = "[Trinix Admin Help Dashboard]"
                embed.add_field(name="**Kicking Members**", value="Command: `.kick <@user>`", inline=False)
                embed.add_field(name="**Banning Members**", value="Command: `.ban <@user> <reason>`", inline=False)
                embed.add_field(name="**Unbanning Members**", value="Command: `.unban <userid>`", inline=False)
                embed.add_field(name="**Purging Messages**", value="Command: `.clean <amount>`", inline=False)
                embed.add_field(name="**Announcing**", value="Command: `.announce <message>`", inline=False)
                embed.add_field(name="**Change Bot Prefix**", value="Command: `.changeprefix <newprefix>`", inline=False)
                embed.set_footer(text="Trinix", icon_url = ctx.guild.icon)
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(title="Trinix Error System", description="[EEROR]You do not have the required permissions.", color=0xff0000)
                await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="[Trinix Error System]", description="[ERROR]This isn't a command.", color=0xff0000)
            await ctx.send(embed=embed)

def setup(bot): #Must have a setup function
    bot.add_cog(help(bot)) # Add the class to the cog.

# --------------------------------------------------------------------------------------------------------------------------------
