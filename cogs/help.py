#Required Imports
import discord, json
from discord.ext import commands, tasks

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def h(self, ctx, arg, cmd=None):
        if arg == "cmd":
            embed = discord.Embed(color=0x7289da)
            embed.title = "Trinix Help . Dashboard"
            embed.add_field(name=":shield: **Admin Commands**", value="Command: `.ahelp`")
            embed.add_field(name=":loud_sound: **Music Commands**", value="Command: `.mhelp`")
            embed.add_field(name=":cyclone: **Misc Commands**", value="Command: `.mishelp`")
            embed.add_field(name=":sparkles: **Neko Commands**", value="Command: `.nhelp`")
            embed.add_field(name=":tada: **Fun Commands**", value="Command: `.fhelp`")
            embed.set_footer(text="Trinix", icon_url = ctx.guild.icon)
            await ctx.send(embed=embed)
        elif arg == "fhelp":
            embed = discord.Embed(color=0x7289da)
            embed.title = "Trinix Fun Help . Dashboard"
            embed.add_field(name="**Random Hello Message**", value="Command: `.hello`", inline=False)
            embed.add_field(name="**Random Message**", value="Command: `.random`", inline=False)
            embed.add_field(name="**Roasting Members**", value="Command: `.roast <@user.none>`", inline=False)
            embed.add_field(name="**Random Ppsize**", value="Command: `.ppsize <@user.none>`", inline=False)
            embed.add_field(name="**Heads Or Tails**", value="Command: `.coinflip`", inline=False)
            embed.add_field(name="**Rating Members Looks**", value="Command: `.rate <@user.none>`", inline=False)
            embed.add_field(name="**Simp Rating Members**", value="Command: `.simprate <@user.none>`", inline=False)
            embed.add_field(name="**Get Truth**", value="Command: `.fun truth`", inline=False)
            embed.add_field(name="**Get Dare**", value="Command: `.fun dare`", inline=False)
            embed.add_field(name="**Get Would You Ratherr**", value="Command: `.fun wyr`", inline=False)
            embed.add_field(name="**Get Never Have I Ever**", value="Command: `.fun nhie`", inline=False)
            embed.add_field(name="**Get Paranoia Question**", value="Command: `.fun nhie`", inline=False)
            embed.set_footer(text="Trinix", icon_url = ctx.guild.icon)
            await ctx.send(embed=embed)
        elif arg == "mhelp":
            embed = discord.Embed(color=0x7289da)
            embed.title = "Trinix Music Help . Dashboard"
            embed.add_field(name="**Playing Music**", value="Command: `.play <name.link>`", inline=False)
            embed.add_field(name="**Looping Music**", value="Command: `.loop` <.loop to unloop>" , inline=False)
            embed.add_field(name="**Bot leave**", value="Command: `.leave`", inline=False)
            embed.add_field(name="**Search Music**", value="Command: `.search <title>`", inline=False)
            embed.add_field(name="**Pausing Music**", value="Command: `.pause`", inline=False)
            embed.add_field(name="**Unpausing Music**", value="Command: `.resume`", inline=False)
            embed.set_footer(text="Trinix", icon_url = ctx.guild.icon)
            await ctx.send(embed=embed)
        elif arg == "mishelp":
            embed = discord.Embed(color=0x7289da)
            embed.title = "Trinix Misc Help . Dashboard"
            embed.add_field(name="**Whois Loop Up**", value="Command: `.whois <@user.none>`", inline=False)
            embed.add_field(name="**Show Bot Uptime**", value="Command: `.uptime`" , inline=False)
            embed.add_field(name="**Show Bot Ping**", value="Command: `.ms`", inline=False)
            embed.add_field(name="Trinix Oauth**", value="Command: `.oauth`", inline=False)
            embed.set_footer(text="Trinix", icon_url = ctx.guild.icon)
            await ctx.send(embed=embed)
        elif arg == "nhelp":
            embed = discord.Embed(color=0x7289da)
            embed.title = "Trinix Neko Help . Dashboard"
            embed.add_field(name="**Hugging Members**", value="Command: `.n hug <@user.none>`", inline=False)
            embed.add_field(name="**Patting Members**", value="Command: `.n pat <@user.none>`", inline=False)
            embed.add_field(name="**Kissing Members**", value="Command: `.n kiss <@user.none>`", inline=False)
            embed.add_field(name="**Slapping Members**", value="Command: `.n slap <@user.none>`", inline=False)
            embed.add_field(name="**Punching Members**", value="Command: `.n punch <@user.none>`", inline=False)
            embed.add_field(name="**Random Nekolewd**", value="Command: `.n nekolewd`", inline=False)
            embed.add_field(name="**Random Kitsune**", value="Command: `.n kitsune`", inline=False)
            embed.add_field(name="**Random Waifu**", value="Command: `.n waifu`", inline=False)
            embed.add_field(name="**Random Neko**", value="Command: `.n neko`", inline=False)
            embed.add_field(name="**Self Crying**", value="Command: `.n cry`", inline=False)
            embed.add_field(name="**Self Smug**", value="Command: `.n smug`", inline=False)
            embed.set_footer(text="Trinix", icon_url = ctx.guild.icon)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ahelp(self, ctx, cmd=None):
        embed = discord.Embed(color=0x7289da)
        embed.title = "Trinix Admin Help . Dashboard"
        embed.add_field(name="**Kicking Members**", value="Command: `.kick <@user>`", inline=False)
        embed.add_field(name="**Banning Members**", value="Command: `.ban <@user> <reason>`", inline=False)
        embed.add_field(name="**Unbanning Members**", value="Command: `.unban <userid>`", inline=False)
        embed.add_field(name="**Purging Messages**", value="Command: `.clean <amount>`", inline=False)
        embed.add_field(name="**Announcing**", value="Command: `.announce <message>`", inline=False)
        embed.add_field(name="**Change Bot Prefix**", value="Command: `.changeprefix <newprefix>`", inline=False)
        embed.set_footer(text="Trinix", icon_url = ctx.guild.icon)
        await ctx.send(embed=embed)

def setup(bot): #Must have a setup function
    bot.add_cog(help(bot)) # Add the class to the cog.