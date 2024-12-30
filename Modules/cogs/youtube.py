from discord import Embed, ui, Button
from discord.ext import commands, tasks
from Modules.database.db import DatabaseManager

import discord, feedparser

class YouTubeNotifier(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db_manager = DatabaseManager()
        self.post_new_videos.start()

    def fetch_latest_video(self, youtube_channel_id):
        """
        Fetches the latest video information for a given YouTube channel.

        Args:
            youtube_channel_id (str): The ID of the YouTube channel.

        Returns:
            tuple: Contains video ID, title, published time, video URL, thumbnail URL, and author name.
            None: If no videos are found for the channel.
        """
        feed = feedparser.parse(f"https://www.youtube.com/feeds/videos.xml?channel_id={youtube_channel_id}")
        if feed.entries:
            latest_video = feed.entries[0]
            video_id = latest_video.id.split(":")[-1]
            title = latest_video.title
            published_at = latest_video.published
            video_url = latest_video.link
            thumbnail_url = latest_video.media_thumbnail[0]['url'] if 'media_thumbnail' in latest_video else None
            author_name = latest_video.author

            return video_id, title, published_at, video_url, thumbnail_url, author_name
        else:
            return None

    @tasks.loop(minutes=10)
    async def post_new_videos(self):
        """
        Periodically checks for new videos and posts notifications to associated Discord channels.

        Uses the database to retrieve configurations and updates the last video ID to avoid duplicate notifications.
        """
        channel_notifications = self.db_manager.execute_read_all_query("SELECT discord_channel_id, youtube_channel_id, last_video_id FROM youtube_notifications")

        for discord_channel_id, youtube_channel_id, last_video_id in channel_notifications:
            latest_video_info = self.fetch_latest_video(youtube_channel_id)
            
            if latest_video_info:
                video_id, title, published_at, video_url, thumbnail_url, author_name = latest_video_info

                if video_id != last_video_id:
                    self.db_manager.execute_query("UPDATE youtube_notifications SET last_video_id = ? WHERE youtube_channel_id = ?", (video_id, youtube_channel_id))

                    channel = self.bot.get_channel(int(discord_channel_id))
                    if channel:
                        embed = discord.Embed(
                            title=title,
                            url=video_url,
                            description=f"{author_name} just uploaded a new video!",
                            color=0x7289da
                        )

                        embed.set_author(name="New Video Alert 🎬", icon_url=thumbnail_url)
                        embed.set_thumbnail(url=thumbnail_url)
                        embed.set_footer(text=f"Published At: {published_at}")

                        view = discord.ui.View()
                        button = discord.ui.Button(label="Watch Now ▶️", style=discord.ButtonStyle.link, url=video_url)
                        view.add_item(button)

                        try:
                            await channel.send(embed=embed, view=view)
                        except Exception as e:
                            print(f"Error posting video {title} to Discord channel {discord_channel_id}: {e}")
                    else:
                        print(f"Discord channel {discord_channel_id} not found")

    @commands.slash_command(description="Link a YouTube channel to this Discord channel for new video notifications.")
    @commands.has_permissions(administrator=True)
    async def add_youtube_channel(self, ctx, youtube_channel_id):
        """
        Links a YouTube channel to the current Discord channel for notifications.

        Args:
            ctx: The context of the command invocation.
            youtube_channel_id (str): The ID of the YouTube channel to link.
        """
        if ctx.guild is None:
            await ctx.respond("This command can only be used in a server's text channel, not in a DM or group chat.", ephemeral=True)
            return
        
        await ctx.defer()

        guild_id = str(ctx.guild.id)
        discord_channel_id = str(ctx.channel.id)
        
        self.db_manager.execute_query("INSERT OR IGNORE INTO youtube_notifications (guild_id, discord_channel_id, youtube_channel_id, last_video_id) VALUES (?, ?, ?, ?)",(guild_id, discord_channel_id, youtube_channel_id, None))

        await ctx.respond(f"Channel ID: `{youtube_channel_id}` notifications set up in {ctx.channel.mention}!", ephemeral=True)

    @commands.slash_command(description="Remove YouTube channel notifications from this Discord channel.")
    @commands.has_permissions(administrator=True)
    async def remove_youtube_channel(self, ctx, youtube_channel_id):
        """
        Removes YouTube channel notifications from the current Discord channel.

        Args:
            ctx: The context of the command invocation.
            youtube_channel_id (str): The ID of the YouTube channel to remove.
        """
        if ctx.guild is None:
            await ctx.respond("This command can only be used in a server's text channel, not in a DM or group chat.", ephemeral=True)
            return
        
        await ctx.defer()

        guild_id = str(ctx.guild.id)
        discord_channel_id = str(ctx.channel.id)

        self.db_manager.execute_query("DELETE FROM youtube_notifications WHERE guild_id = ? AND discord_channel_id = ? AND youtube_channel_id = ?", (guild_id, discord_channel_id, youtube_channel_id))
        
        await ctx.respond(f"Channel ID: `{youtube_channel_id}` notifications removed from {ctx.channel.mention}!", ephemeral=True)

def setup(bot):
    bot.add_cog(YouTubeNotifier(bot))
