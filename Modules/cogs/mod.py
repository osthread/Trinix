"""
Setting Up Bot Permissions

If the bot isn't kicking or banning members as expected, it's likely due to a permissions issue. Follow these steps to resolve it:

1. **Check Role Hierarchy**:
   - Open your server settings.
   - Navigate to the "Roles" tab.
   - Ensure the bot's role (e.g., "Trinix") is positioned **above** the roles of the members it needs to manage.

2. **Create a Bot Role (Optional)**:
   - If no specific role exists for the bot, create one (e.g., "Bot Role").
   - Assign this new role to the bot.
   - Position this role **above** the member roles in the hierarchy.

3. **Save Changes**:
   - After adjusting the role hierarchy, make sure to save the changes.

By ensuring the bot's role is higher than the roles of the members it needs to moderate, the bot will have the necessary permissions to perform actions like kicking or banning users.
"""

from discord.ext import commands
from discord.ui import View, Button

from Modules.database.db import DatabaseManager

import discord

class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db_manager = DatabaseManager()

    @commands.slash_command(description="Show all available commands")
    async def help(self, ctx):
        """
        Displays a paginated help menu showing all available bot commands.

        Args:
            ctx: The context of the command invocation.

        Paginated categories include:
        - AI and Fun Commands
        - Media Commands
        - YouTube Notifications
        - Music Commands
        - Moderation Commands
        """

        await ctx.defer()

        class HelpPaginator(View):
            """
            A paginated view for navigating through help embeds.

            Args:
                embeds (list): A list of embed objects for different categories.
            """

            def __init__(self, embeds):
                super().__init__(timeout=None)
                self.embeds = embeds
                self.current_page = 0

                self.next_button = Button(label="Next", style=discord.ButtonStyle.primary)
                self.prev_button = Button(label="Previous", style=discord.ButtonStyle.primary)
                self.next_button.callback = self.next_page
                self.prev_button.callback = self.prev_page

                self.add_item(self.prev_button)
                self.add_item(self.next_button)
                self.update_buttons()

            def update_buttons(self):
                """
                Updates button states based on the current page.
                """
                self.prev_button.disabled = self.current_page <= 0
                self.next_button.disabled = self.current_page >= len(self.embeds) - 1

            async def next_page(self, interaction):
                """
                Advances to the next page.
                """
                self.current_page += 1
                self.update_buttons()
                await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)

            async def prev_page(self, interaction):
                """
                Returns to the previous page.
                """

                self.current_page -= 1
                self.update_buttons()
                await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)

        embeds = []

        # AI and Fun Commands
        embed_ai_fun = discord.Embed(
            title="AI and Fun Commands",
            description=(
                "`/chat` - Interact with Trinix AI using selected models.\n"
                "`/neko` - Perform fun neko actions with or without tagging others.\n"
                "`/fun` - Enjoy activities like truth, dare, or paranoia prompts."
            ),
            color=0x7289da
        )
        embed_ai_fun.set_thumbnail(url="https://cdn.discordapp.com/emojis/1319528120205967401.png")
        embeds.append(embed_ai_fun)

        # Media Commands
        embed_media = discord.Embed(
            title="Media Commands",
            description=(
                "`/search` - Search for movies or TV shows.\n"
                "`/trending_movies` - View the top 5 trending movies.\n"
                "`/trending_tv_shows` - View the top 5 trending TV shows."
            ),
            color=0x7289da
        )
        embed_media.set_thumbnail(url="https://cdn.discordapp.com/emojis/1319528120205967401.png")
        embeds.append(embed_media)

        # YouTube Notifications
        embed_youtube = discord.Embed(
            title="YouTube Notifications",
            description=(
                "`/add_youtube_channel` - Link a YouTube channel.\n"
                "`/remove_youtube_channel` - Remove YouTube channel."
            ),
            color=0x7289da
        )
        embed_youtube.set_thumbnail(url="https://cdn.discordapp.com/emojis/1319528120205967401.png")
        embeds.append(embed_youtube)

        # Moderation Commands
        embed_moderation = discord.Embed(
            title="Moderation Commands",
            description=(
                "`/clone_channel` - Clone the current channel.\n"
                "`/setup_logger` - Set up a log channel for the server.\n"
                "`/enable` - Enable logging (voice, message, or join detection).\n"
                "`/disable` - Disable logging (voice, message, or join detection).\n"
                "`/clean` - Bulk delete messages in a channel.\n"
                "`/kick` - Kick a member from the server.\n"
                "`/ban` - Ban a member from the server.\n"
                "`/lock` - Lock the current channel.\n"
                "`/unlock` - Unlock the current channel.\n"
            ),
            color=0x7289da
        )
        embed_moderation.set_thumbnail(url="https://cdn.discordapp.com/emojis/1319528120205967401.png")
        embeds.append(embed_moderation)

        view = HelpPaginator(embeds)
        await ctx.respond(embed=embeds[0], view=view)

    @commands.slash_command(description="Clone the current channel and delete the original one.")
    @commands.has_permissions(manage_channels=True)
    async def clone_channel(self, ctx):
        """
        Clones the current channel and deletes the original.

        Args:
            ctx: The context of the command invocation.
        """

        await ctx.defer()
        channel = ctx.channel

        try:
            new_channel = await channel.clone(reason=f"Cloned by {ctx.author}")
            await new_channel.edit(position=channel.position)
            await channel.delete(reason=f"Channel replaced by {ctx.author}")
            await new_channel.send(f"{ctx.author.mention} cloned and replaced this channel successfully.", delete_after=10)
        except Exception as e:
            await ctx.respond(f"An error occurred: {str(e)}", ephemeral=True)

    @commands.slash_command(description="Configure a log channel for the server.")
    @commands.has_permissions(administrator=True)
    async def setup_logger(self, ctx):
        """
        Configures a log channel for server events.

        Args:
            ctx: The context of the command invocation.
        """

        await ctx.defer()

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
                self.db_manager.execute_query(f"UPDATE config SET webhook='{mg_webhook.url}' WHERE guild_id = ?", (ctx.guild.id,))
            except:
                await ctx.respond('Something went wrong.')
 
            await ctx.respond('Log server has been setup.')

    @commands.slash_command(description="Lock the current channel.")
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
        """
        Locks the current channel, preventing default role from sending messages.

        Args:
            ctx: The context of the command invocation.
        """

        channel = ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.respond(f"{channel.mention} is now locked.", delete_after=10)

    @commands.slash_command(description="Unlock the current channel.")
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        """
        Unlocks the current channel, allowing the default role to send messages.

        Args:
            ctx: The context of the command invocation.
        """

        channel = ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.respond(f"{channel.mention} is now unlocked.", delete_after=10)

    @commands.slash_command(description="Enable specific logging or monitoring features.")
    @commands.has_permissions(administrator=True)
    async def enable(self, ctx, option: discord.Option(str, "Choose a option!", choices=["voice", "message", "join"])): 
        """
        Enables a specific monitoring feature.

        Args:
            ctx: The context of the command invocation.
            option: The feature to enable (voice, message, or join).
        """

        res = self.db_manager.execute_read_one_query("SELECT voice_logger,message_logger FROM config WHERE guild_id = ?", (ctx.guild.id,))
        if option.lower() == "voice":
            if res[0] == "on":
                return await ctx.respond("Voice Monitor has already been enabled.")

            self.db_manager.execute_query("UPDATE config SET voice_logger = 'on' WHERE guild_id = ?", (ctx.guild.id,))
            embed = discord.Embed(title="[Mod System] Message Logger", description="Voice logger has been enabled!", color=0x00FF00)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1319528120205967401.png")
            embed.set_footer(text = ctx.guild.name, icon_url = self.bot.user.avatar)
            await ctx.respond(embed=embed)

        elif option.lower() == "message":
            if res[1] == "on":
                return await ctx.respond("Message Logger has already been enabled.")

            self.db_manager.execute_query("UPDATE config SET message_logger = 'on' WHERE guild_id = ?", (ctx.guild.id,))
            embed = discord.Embed(title="[Mod System] Message Logger", description="Message logger has been enabled!", color=0x00FF00)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1319528120205967401.png")
            embed.set_footer(text = ctx.guild.name, icon_url = self.bot.user.avatar)
            await ctx.respond(embed=embed)

        elif option.lower() == "join":
            if res[1] == "on":
                return await ctx.respond("Join Detection has already been enabled.")

            self.db_manager.execute_query("UPDATE config SET join_detection = 'on' WHERE guild_id = ?", (ctx.guild.id,))
            embed = discord.Embed(title="[Mod System] Join Detection", description="Join Detection has been enabled!", color=0x00FF00)
            embed.set_footer(text = ctx.guild.name, icon_url = self.bot.user.avatar)
            await ctx.respond(embed=embed)

    @commands.slash_command(description="Disable specific logging or monitoring features.")
    @commands.has_permissions(administrator=True)
    async def disable(self, ctx, option: discord.Option(str, "Choose a option!", choices=["voice", "message", "join"])): 
        """
        Disables a specific monitoring feature.

        Args:
            ctx: The context of the command invocation.
            option: The feature to disable (voice, message, or join).
        """

        await ctx.defer()

        res = self.db_manager.execute_read_one_query("SELECT voice_logger,message_logger FROM config WHERE guild_id = ?", (ctx.guild.id,))

        if option.lower() == "voice":
            if res[0] == "off":
                return await ctx.respond("Voice Monitor has already been disabled.")

            self.db_manager.execute_query("UPDATE config SET voice_logger = 'off' WHERE guild_id = ?", (ctx.guild.id,))
            embed = discord.Embed(title="[Mod System] Voice logger", description="Voice logger has been disabled!", color=0x00FF00)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1319528120205967401.png")
            embed.set_footer(text = ctx.guild.name, icon_url = self.bot.user.avatar)
            await ctx.respond(embed=embed)

        elif option.lower() == "message":
            if res[1] == "off":
                return await ctx.respond("Message Logger has already been disabled.")

            self.db_manager.execute_query("UPDATE config SET message_logger = 'off' WHERE guild_id = ?", (ctx.guild.id,))
            embed = discord.Embed(title="[Mod System] Message Logger", description="Message logger has been disabled!", color=0x00FF00)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1319528120205967401.png")
            embed.set_footer(text = ctx.guild.name, icon_url = self.bot.user.avatar)
            await ctx.respond(embed=embed)

        elif option.lower() == "join":
            if res[1] == "off":
                return await ctx.respond("Join Detection has already been disabled.")

            self.db_manager.execute_query("UPDATE config SET join_detection = 'off' WHERE guild_id = ?", (ctx.guild.id,))
            embed = discord.Embed(title="[Mod System] Join Detection", description="Join Detection has been disabled!", color=0x00FF00)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1319528120205967401.png")
            embed.set_footer(text = ctx.guild.name, icon_url = self.bot.user.avatar)
            await ctx.respond(embed=embed)

    @commands.slash_command(description="Bulk delete a specified number of messages from the current channel.")
    @commands.has_permissions(administrator=True)
    async def clean(self, ctx, limit: int):
        """
        Bulk deletes a specified number of messages from the current channel.

        Args:
            ctx: The context of the command invocation.
            limit: The number of messages to delete.
        """

        await ctx.defer()

        await ctx.channel.purge(limit=limit)

        embed = discord.Embed(title="[Mod System] Chat Purge", description=f"{ctx.author.mention} Deleted {limit} messages.", color=0x00FF00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1319528120205967401.png")
        embed.set_footer(text = ctx.guild.name, icon_url = self.bot.user.avatar)
        await ctx.respond(embed=embed, delete_after=5)

    @commands.slash_command(description="Remove a member from the server. ")
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, reason = None):
        """
        Kicks a member from the server.

        Args:
            ctx: The context of the command invocation.
            member: The member to kick.
            reason: The reason for the kick (optional).
        """

        await ctx.defer()

        if reason == "None":
            await member.kick(reason = "None")
        else:
            await member.kick(reason=reason)
        embed=discord.Embed(title="[Mod System] Kick Member", description=f"{member.mention} has been kicked from this server by {ctx.author.mention}", color=0x00FF00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1319528120205967401.png")
        embed.add_field(name="Reason", value=f"{reason}")
        await ctx.respond(embed=embed)

    @commands.slash_command(description="Permanently ban a member from the server.")
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, reason = None):
        """
        Bans a member from the server.

        Args:
            ctx: The context of the command invocation.
            member: The member to ban.
            reason: The reason for the ban (optional).
        """

        await ctx.defer()

        if reason == None:
            await member.ban(reason = "None")
        else:
            await member.ban(reason = "None")
        embed=discord.Embed(title="[Mod System] Ban Member", description=f"{member.mention} has been Banned from this server by {ctx.author.mention}", color=0x00FF00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1319528120205967401.png")
        embed.add_field(name="Reason", value=f"{reason}")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(mod(bot))
