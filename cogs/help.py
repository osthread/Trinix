#Required Imports
import discord
from discord.ext import commands, tasks, json

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, cmd=None):
        embed = discord.Embed()
        embed.title = "Trinix Help / Dashboard"
        embed.add_field(name=":shield: **Admin Commands**", value="Command: `.ahelp`")
        embed.add_field(name=":loud_sound: **Music Commands**", value="Command: `.mhelp`")
        embed.add_field(name=":cyclone: **Misc Commands**", value="Command: `.mishelp`")
        embed.add_field(name=":sparkles: **Neko Commands**", value="Command: `.nhelp`")
        embed.add_field(name=":tada: **Fun Commands**", value="Command: `.fhelp`")
        embed.set_thumbnail(url= ctx.guild.icon_url)
        embed.set_footer(text="Trinix", icon_url = ctx.guild.icon_url)
        embed.color = discord.Color.blurple()
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def ahelp(self, ctx, cmd=None):
        embed = discord.Embed()
        embed.title = "Trinix Admin Help / Dashboard"
        embed.add_field(name="**Kicking Members**", value="Command: `.kick <@user>`", inline=False)
        embed.add_field(name="**Banning Members**", value="Command: `.ban <@user> <reason>`", inline=False)
        embed.add_field(name="**Unbanning Members**", value="Command: `.unban <userid>`", inline=False)
        embed.add_field(name="**Purging Messages**", value="Command: `.purge <amount>`", inline=False)
        embed.add_field(name="**Announcing**", value="Command: `.announce <message>`", inline=False)
        embed.add_field(name="**Change Server Prefix**", value="Command: `.changeprefix <newprefix>`", inline=False)
        embed.set_thumbnail(url= ctx.guild.icon_url)
        embed.set_footer(text="Trinix", icon_url = ctx.guild.icon_url)
        embed.color = discord.Color.blurple()
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def fhelp(self, ctx, cmd=None):
        embed = discord.Embed()
        embed.title = "Trinix Fun Help / Dashboard"
        embed.add_field(name="**Random Hello Message**", value="Command: `.hello`", inline=False)
        embed.add_field(name="**Random Message**", value="Command: `.random`", inline=False)
        embed.add_field(name="**Roasting Members**", value="Command: `.roast <@user/none>`", inline=False)
        embed.add_field(name="**Random Ppsize**", value="Command: `.ppsize <@user/none>`", inline=False)
        embed.add_field(name="**Heads Or Tails**", value="Command: `.coinflip`", inline=False)
        embed.add_field(name="**Rating Members Looks**", value="Command: `.rate <@user/none>`", inline=False)
        embed.add_field(name="**Simp Rating Members**", value="Command: `.simprate <@user/none>`", inline=False)
        embed.add_field(name="**Get Truth**", value="Command: `.truth`", inline=False)
        embed.add_field(name="**Get Dare**", value="Command: `.dare`", inline=False)
        embed.add_field(name="**Get Would You Ratherr**", value="Command: `.wyr`", inline=False)
        embed.add_field(name="**Get Never Have I Ever**", value="Command: `.nhie`", inline=False)
        embed.add_field(name="**Get Paranoia Question**", value="Command: `.nhie`", inline=False)
        embed.set_thumbnail(url= ctx.guild.icon_url)
        embed.set_footer(text="Trinix", icon_url = ctx.guild.icon_url)
        embed.color = discord.Color.blurple()
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def mhelp(self, ctx, cmd=None):
        embed = discord.Embed()
        embed.title = "Trinix Music Help / Dashboard"
        embed.add_field(name="**Playing Music**", value="Command: `.play <name/link>`", inline=False)
        embed.add_field(name="**Looping Music**", value="Command: `.loop` <.loop to unloop>" , inline=False)
        embed.add_field(name="**Bot leave**", value="Command: `.leave`", inline=False)
        embed.add_field(name="**Search Music**", value="Command: `.search <title>`", inline=False)
        embed.add_field(name="**Pausing Music**", value="Command: `.pause`", inline=False)
        embed.add_field(name="**Unpausing Music**", value="Command: `.resume`", inline=False)
        embed.set_thumbnail(url= ctx.guild.icon_url)
        embed.set_footer(text="Trinix", icon_url = ctx.guild.icon_url)
        embed.color = discord.Color.blurple()
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def mishelp(self, ctx, cmd=None):
        embed = discord.Embed()
        embed.title = "Trinix Misc Help / Dashboard"
        embed.add_field(name="**Whois Loop Up**", value="Command: `.whois <@user/none>`", inline=False)
        embed.add_field(name="**Show Bot Uptime**", value="Command: `.uptime`" , inline=False)
        embed.add_field(name="**Show Bot Ping**", value="Command: `.ms`", inline=False)
        embed.add_field(name="**Trinix Bot Website**", value="Command: `.website`", inline=False)
        embed.add_field(name="Trinix Oauth**", value="Command: `.oauth`", inline=False)
        embed.add_field(name="Password Generator**", value="Command: `.oauth`", inline=False)
        embed.set_thumbnail(url= ctx.guild.icon_url)
        embed.set_footer(text="Trinix", icon_url = ctx.guild.icon_url)
        embed.color = discord.Color.blurple()
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def nhelp(self, ctx, cmd=None):
        embed = discord.Embed()
        embed.title = "Trinix Neko Help / Dashboard"
        embed.add_field(name="**Hugging Members**", value="Command: `.hug <@user/none>`", inline=False)
        embed.add_field(name="**Patting Members**", value="Command: `.pat <@user/none>`", inline=False)
        embed.add_field(name="**Kissing Members**", value="Command: `.kiss <@user/none>`", inline=False)
        embed.add_field(name="**Slapping Members**", value="Command: `.slap <@user/none>`", inline=False)
        embed.add_field(name="**Punching Members**", value="Command: `.punch <@user/none>`", inline=False)
        embed.add_field(name="**Random Nekolewd**", value="Command: `.nekolewd`", inline=False)
        embed.add_field(name="**Random Kitsune**", value="Command: `.kitsune`", inline=False)
        embed.add_field(name="**Random Waifu**", value="Command: `.waifu`", inline=False)
        embed.add_field(name="**Random Neko**", value="Command: `.neko`", inline=False)
        embed.add_field(name="**Self Crying**", value="Command: `.cry`", inline=False)
        embed.add_field(name="**Self Smug**", value="Command: `.smug`", inline=False)
        embed.set_thumbnail(url= ctx.guild.icon_url)
        embed.set_footer(text="Trinix", icon_url = ctx.guild.icon_url)
        embed.color = discord.Color.blurple()
        await ctx.reply(embed=embed, mention_author=False)

def setup(bot): #Must have a setup function
    bot.add_cog(help(bot)) # Add the class to the cog.
