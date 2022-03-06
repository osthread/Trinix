#Required Imports
from discord.ext import commands, tasks
import discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, cmd=None):
        embed = discord.Embed()
        embed.title = "Trinix Help / Dashboard"
        embed.add_field(name=":globe_with_meridians: **Fun**", value="`hello`,`ppsize`,`roast`,`random`,`coinflip`,`rate`,`simprate`", inline=False)
        embed.add_field(name=":loud_sound: **Music**", value="`play`,`pause`,`leave`,`resume`,`remove`,`queue`,`join`,`skip`", inline=False)
        embed.add_field(name=":shield: **Mod**", value="`kick`,`ban`,`purge`,`unban`", inline=False)
        embed.add_field(name=":cyclone: **Misc**", value="`oauth`,`ping`,`uptime`,`userinfo`,`website`,`passgen`", inline=False)
        embed.add_field(name=":slight_smile: **Emotes**", value="`laugh`,`mad`,`bye`,`blush`,`sneeze`,`smile`,`thinking`", inline=False)
        embed.add_field(name=":hugging: **Actions**", value="`cuddle`,`feed`,`hug`,`kickk`,`kiss`,`pat`,`punch`,`slap`,`poke`,`dance`,`squeeze`,`handholding`", inline=False)
        embed.add_field(name=":newspaper: **News**", value="If Trinix isn't playing music please do .stop and replay the song.", inline=False)
        embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/888282878973194271/891935435859820574/default.png")
        embed.set_footer(text="Trinix Made by: Maxim", icon_url = "https://cdn.discordapp.com/attachments/888282878973194271/891935435859820574/default.png")
        embed.color = discord.Color.blurple()
        await ctx.reply(embed=embed, mention_author=False)

def setup(bot): #Must have a setup function
    bot.add_cog(Help(bot)) # Add the class to the cog.
