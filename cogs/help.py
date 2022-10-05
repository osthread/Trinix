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
                embed.add_field(name=":shield: **Admin Commands**", value="Command: `.help admin`")
            embed.add_field(name=":loud_sound: **Music Commands**", value="Command: `.help music`")
            embed.add_field(name=":cyclone: **Misc Commands**", value="Command: `.help misc`")
            embed.add_field(name=":sparkles: **Neko Commands**", value="Command: `.help neko`")
            embed.add_field(name=":tada: **Fun Commands**", value="Command: `.help fun`")
            embed.set_footer(text="Trinix", icon_url = ctx.guild.icon)
            await ctx.send(embed=embed)

        elif arg == "fun":
            embed = discord.Embed(color=0x7289da)
            embed.title = "[Trinix Fun Help Dashboard]"
            embed.add_field(name="**Random Hello Message**", value="Command: `.hello`")
            embed.add_field(name="**Random Message**", value="Command: `.random`")
            embed.add_field(name="**Roasting Members**", value="Command: `.roast <@user>`")
            embed.add_field(name="**Random Ppsize**", value="Command: `.ppsize <@user>`")
            embed.add_field(name="**Heads Or Tails**", value="Command: `.coinflip`")
            embed.add_field(name="**Rating Members Looks**", value="Command: `.rate <@user>`")
            embed.add_field(name="**Simp Rating Members**", value="Command: `.simprate <@user>`")
            embed.add_field(name="**Get Truth**", value="Command: `.fun truth`")
            embed.add_field(name="**Get Dare**", value="Command: `.fun dare`")
            embed.add_field(name="**Get Would You Ratherr**", value="Command: `.fun wyr`")
            embed.add_field(name="**Get Never Have I Ever**", value="Command: `.fun nhie`")
            embed.add_field(name="**Get Paranoia Question**", value="Command: `.fun nhie`")
            embed.set_footer(text="Trinix", icon_url = ctx.guild.icon)
            await ctx.send(embed=embed)

        elif arg == "music":
            embed = discord.Embed(color=0x7289da)
            embed.title = "[Trinix Music Help Dashboard]"
            embed.add_field(name="**Playing Music**", value="Command: `.play <name.link>`")
            embed.add_field(name="**Looping Music**", value="Command: `.loop` <.loop to unloop>" )
            embed.add_field(name="**Bot leave**", value="Command: `.leave`")
            embed.add_field(name="**Search Music**", value="Command: `.search <title>`")
            embed.add_field(name="**Pausing Music**", value="Command: `.pause`")
            embed.add_field(name="**Unpausing Music**", value="Command: `.resume`")
            embed.set_footer(text="Trinix", icon_url = ctx.guild.icon)
            await ctx.send(embed=embed)

        elif arg == "misc":
            embed = discord.Embed(color=0x7289da)
            embed.title = "[Trinix Misc Help Dashboard]"
            embed.add_field(name="how Bot Uptime", value="Command: `.uptime`", inline=False)
            embed.add_field(name="Show Bot Ping", value="Command: `.ms`", inline=False)
            embed.add_field(name="Trinix Oauth", value="Command: `.oauth`", inline=False)
            embed.set_footer(text="Trinix", icon_url = ctx.guild.icon)
            await ctx.send(embed=embed)

        elif arg == "neko":
            embed = discord.Embed(color=0x7289da)
            embed.title = "[Trinix Neko Help Dashboard]"
            embed.add_field(name="**Hugging Members**", value="Command: `.n hug <@user>`")
            embed.add_field(name="**Patting Members**", value="Command: `.n pat <@user>`")
            embed.add_field(name="**Kissing Members**", value="Command: `.n kiss <@user>`")
            embed.add_field(name="**Slapping Members**", value="Command: `.n slap <@user>`")
            embed.add_field(name="**Punching Members**", value="Command: `.n punch <@user>`")
            embed.add_field(name="**Random Nekolewd**", value="Command: `.n nekolewd`")
            embed.add_field(name="**Random Kitsune**", value="Command: `.n kitsune`")
            embed.add_field(name="**Random Waifu**", value="Command: `.n waifu`")
            embed.add_field(name="**Random Neko**", value="Command: `.n neko`")
            embed.add_field(name="**Self Crying**", value="Command: `.n cry`")
            embed.add_field(name="**Self Smug**", value="Command: `.n smug`")
            embed.set_footer(text="Trinix", icon_url = ctx.guild.icon)
            await ctx.send(embed=embed)
        elif arg == "admin":
            if ctx.message.author.guild_permissions.administrator:
                embed = discord.Embed(color=0x7289da)
                embed.title = "[Trinix Admin Help Dashboard]"
                embed.add_field(name="**Kicking Members**", value="Command: `.kick <@user>`")
                embed.add_field(name="**Banning Members**", value="Command: `.ban <@user> <reason>`")
                embed.add_field(name="**Unbanning Members**", value="Command: `.unban <userid>`")
                embed.add_field(name="**Purging Messages**", value="Command: `.clean <amount>`")
                embed.add_field(name="**Announcing**", value="Command: `.announce <message>`")
                embed.add_field(name="**Change Bot Prefix**", value="Command: `.changeprefix <newprefix>`")
                embed.set_footer(text="Trinix", icon_url = ctx.guild.icon)
                await ctx.send(embed=embed)
            else:
                await ctx.send('You arent allowed to use this command.')
        else:
            embed=discord.Embed(title="[Trinix Error System]", description="[ERROR]This isn't a command.", color=0xff0000)
            await ctx.send(embed=embed)

def setup(bot): #Must have a setup function
    bot.add_cog(help(bot)) # Add the class to the cog.

# --------------------------------------------------------------------------------------------------------------------------------
