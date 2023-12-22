# Please mind if the bot isnt kicking or banning any members its probably because the bot is below the members. Move Trinix role or make a bot role
# and put it above the members. 

from discord.ext import commands, tasks

from Modules.database.db import DatabaseManager

import discord

class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db_manager = DatabaseManager()

    @commands.slash_command(description="Setup log channel")
    @commands.has_permissions(administrator=True)
    async def setup_logger(self, ctx):
        guild = ctx.guild
        ch = discord.utils.get(guild.channels, name="logger")
        if ch:
            await ctx.respond('Channels are already setup.')
            return
        else:
            category = await guild.create_category("logs")
            overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False)}
            msg = await category.create_text_channel("logger", overwrites=overwrites)
            mg_webhook = await msg.create_webhook(name=f"{msg}_webhook")
            try:
                self.db_manager.execute_query(f"UPDATE config SET webhook='{mg_webhook.url}' WHERE guild_id = {ctx.guild.id}")
            except:
                await ctx.respond('Something went wrong.')
 
            await ctx.respond('Log server has been setup.')

    @commands.slash_command(description="Enable logger")
    @commands.has_permissions(administrator=True)
    async def enable(self, ctx, option: Option(str, "Choose a option!", choices=["voice", "message"])): 
        if option.lower() == "voice":
            self.db_manager.execute_query("UPDATE config SET voice_logger = 'on'")
            embed = discord.Embed(title="[Mod System] Message Logger", description="Voice logger has been enabled!", color=0x00FF00)
            embed.set_footer(text = ctx.guild.name, icon_url = self.bot.user.avatar)
            await ctx.respond(embed=embed)

        elif option.lower() == "message":
            self.db_manager.execute_query("UPDATE config SET message_logger = 'on'")
            embed = discord.Embed(title="[Mod System] Message Logger", description="Message logger has been enabled!", color=0x00FF00)
            embed.set_footer(text = ctx.guild.name, icon_url = self.bot.user.avatar)
            await ctx.respond(embed=embed)

    @commands.slash_command(description="Disable logger")
    @commands.has_permissions(administrator=True)
    async def disable(self, ctx, option: Option(str, "Choose a option!", choices=["voice", "message"])): 
        if option.lower() == "voice":
            self.db_manager.execute_query("UPDATE config SET voice_logger = 'off'")
            embed = discord.Embed(title="[Mod System] Voice logger", description="Voice logger has been disabled!", color=0x00FF00)
            embed.set_footer(text = ctx.guild.name, icon_url = self.bot.user.avatar)
            await ctx.respond(embed=embed)

        elif option.lower() == "message":
            self.db_manager.execute_query("UPDATE config SET message_logger = 'off'")
            embed = discord.Embed(title="[Mod System] Message Logger", description="Message logger has been disabled!", color=0x00FF00)
            embed.set_footer(text = ctx.guild.name, icon_url = self.bot.user.avatar)
            await ctx.respond(embed=embed)

    @commands.slash_command(description="Clean channel")
    @commands.has_permissions(administrator=True)
    async def clean(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        embed = discord.Embed(title="[Mod System] Chat Purge", description=f"{ctx.author.mention} Deleted {limit} messages.", color=0x00FF00)
        embed.set_footer(text = ctx.guild.name, icon_url = self.bot.user.avatar)
        await ctx.respond(embed=embed, delete_after=5)

    @commands.slash_command(description="Kick a member")
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, reason = None):
        if reason == "None":
            await member.kick(reason = "None")
        else:
            await member.kick(reason=reason)
        embed=discord.Embed(title="[Mod System] Kick Member", description=f"{member.mention} has been kicked from this server by {ctx.author.mention}", color=0x00FF00)
        embed.add_field(name="Reason", value=f"{reason}")
        await ctx.respond(embed=embed)

    @commands.slash_command(description="Ban a member")
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, reason = None):
        if reason == None:
            await member.ban(reason = "None")
        else:
            await member.ban(reason = "None")
        embed=discord.Embed(title="[Mod System] Ban Member", description=f"{member.mention} has been Banned from this server by {ctx.author.mention}", color=0x00FF00)
        embed.add_field(name="Reason", value=f"{reason}")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(mod(bot))
