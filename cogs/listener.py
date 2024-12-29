from datetime import datetime
from discord import message, Webhook
from discord.ext import commands

from Modules.database.db import DatabaseManager

import discord, aiohttp

class listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.timestamp = datetime.utcnow().strftime('%Y-%m-%d %I:%M:%S %p UTC')
        self.db_manager = DatabaseManager()

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name="JuiceWRLD"))

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx: discord.ApplicationContext, error: discord.DiscordException):
        if isinstance(error, commands.MissingRole):
            return await ctx.respond(f"You are missing the required roles to use this command.", ephemeral=True)
            
        elif isinstance(error, commands.MissingPermissions):
            return await ctx.respond(f"You are missing the required permissions", ephemeral=True)
            
        await ctx.respond("An error occurred: {}".format(str(error)), ephemeral=True)
            
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        self.db_manager.execute_query(f"INSERT INTO config (guild_id, webhook, message_logger, voice_logger, join_detection) VALUES ('{guild.id}', 'None', 'off', 'off', 'off')")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        self.db_manager.execute_query(f"DELETE FROM config WHERE guild_id = '{guild.id}'")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        member_join = self.db_manager.execute_read_one_query("SELECT join_detection, webhook, guild_id FROM config WHERE guild_id = ?", (member.guild.id,))
        if member_join and member_join[0] == "on" and member.guild.id == int(member_join[2]):
            if member.bot:
                return  

            embed = discord.Embed(title='Server Monitor', color=0x7289da)
            embed.set_author(name=f'Guild: {member.guild.name}', icon_url=self.bot.user.avatar.url)
            embed.set_footer(text=f"Trinix Assistant | {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}")

            suspicious = False
            reasons = []

            if not member.avatar:
                reasons.append('No profile picture')

            if suspicious:
                async with aiohttp.ClientSession() as session:
                    webhook = discord.Webhook.from_url(member_join[1], session=session)
                    await webhook.send(embed=embed, username='Trinix')

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return

        if message.author.id == self.bot.user.id:
            return
        try:
            msg_log = self.db_manager.execute_read_one_query("SELECT message_logger, webhook, guild_id FROM config WHERE guild_id = ?", (message.guild.id,))
            if msg_log[0] == "on" and message.guild.id == int(msg_log[2]):
                embed = discord.Embed(title='Server Monitor', description=f'Message deleted in: {message.channel.mention}', color=0x7289da)
                embed.set_author(name=f'Guild: {message.guild}', url='https://discord.gg/WTEVegPfRv', icon_url=self.bot.user.avatar)
                if message.attachments:
                    if message.content:
                        embed.add_field(name='Message Deleted', value=f'{message.content}')
                        embed.add_field(name='File Deleted', value=f"[Download]({message.attachments[0].url})")
                    else:
                        embed.add_field(name='File Deleted', value=f"[Download]({message.attachments[0].url})")
                else:
                    embed.add_field(name='Message Deleted', value=f'{message.content}')
                embed.add_field(name='Member', value=f'{message.author.mention}', inline=False)
                embed.set_footer(text=f"Trinix Assistant | {self.timestamp}")
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(msg_log[1], session=session)
                    await webhook.send(embed=embed, username='Trinix')
        except:
            pass

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.bot or after.author.bot:
            return

        if before.author.id == self.bot.user.id or after.author.id == self.bot.user.id:
            return

        try:
            msg_log = self.db_manager.execute_read_one_query("SELECT message_logger, webhook, guild_id FROM config WHERE guild_id = ?", (message.guild.id,))
            if msg_log[0] == "on" and message.guild.id == int(msg_log[2]):
                embed=discord.Embed(title='Server Monitor', description=f'Message Edited In {after.channel.mention}', color=0x7289da)
                embed.set_author(name=f'Guild: {before.guild}', url='https://discord.gg/WTEVegPfRv', icon_url=self.bot.user.avatar)
                embed.add_field(name='Before', value=before.content)
                embed.add_field(name='After', value=after.content)
                embed.add_field(name='Member', value=f'{after.author.mention}', inline=False)  
                embed.set_footer(text=f"Trinix Assistant | {self.timestamp }")
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(msg_log[1], session=session)
                    await webhook.send(embed=embed, username='Trinix')
        except:
            pass

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member.bot:
            return

        if member.id == self.bot.user.id:
            return

        try:
            try:
                vlogger = self.db_manager.execute_read_one_query(f"SELECT voice_logger, webhook, guild_id FROM config WHERE guild_id = ?", (before.channel.guild.id,))
            except:
                vlogger = self.db_manager.execute_read_one_query(f"SELECT voice_logger, webhook, guild_id FROM config WHERE guild_id = ?", (after.channel.guild.id,))

            if vlogger[0] == "on":
                embed = discord.Embed(title='Server Monitor', color=0x7289da)
                embed.set_author(name=f'Guild: {member.guild}', url='https://discord.gg/WTEVegPfRv', icon_url=self.bot.user.avatar)
                embed.set_footer(text=f"Trinix Assistant | {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}", icon_url=self.bot.user.avatar)

                if before.channel != after.channel:
                    # User switched channels
                    if before.channel and after.channel:
                        embed.description = f'{member.mention} moved voice channels.'
                        embed.add_field(name='Voice Channels', value=f'{before.channel.mention} -> {after.channel.mention}')
                    # User joined a channel
                    elif after.channel:
                        embed.description = f'{member.mention} joined a voice channel.'
                        embed.add_field(name='Voice Channel', value=after.channel.mention)
                    # User left a channel
                    elif before.channel:
                        embed.description = f'{member.mention} left a voice channel.'
                        embed.add_field(name='Voice Channel', value=before.channel.mention)

                elif before.channel == after.channel:
                    # Mute, Deafen, Stream, Video, AFK status changes
                    if after.self_deaf != before.self_deaf:
                        embed.description = f'{member.mention} {"deafened" if after.self_deaf else "undeafened"} themselves.'
                    elif after.self_mute != before.self_mute:
                        embed.description = f'{member.mention} {"muted" if after.self_mute else "unmuted"} themselves.'
                    elif after.self_stream != before.self_stream:
                        embed.description = f'{member.mention} {"started" if after.self_stream else "stopped"} streaming.'
                    elif after.self_video != before.self_video:
                        embed.description = f'{member.mention} {"turned on" if after.self_video else "turned off"} their camera.'
                    elif after.afk != before.afk:
                        embed.description = f'{member.mention} {"went AFK" if after.afk else "returned from AFK"}.'

                if embed.description:
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(vlogger[1], session=session)
                        await webhook.send(embed=embed, username='Trinix')
        except:
            pass
        
def setup(bot): 
    bot.add_cog(listener(bot))
