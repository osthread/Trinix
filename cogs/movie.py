from discord.ext import commands, tasks
from discord.ui import Modal, View

from Modules.database.db import DatabaseManager

import requests, discord

class SelectMovie(discord.ui.View):
    def __init__(self, options):
        super().__init__(timeout=None)
        select_options = [
            discord.SelectOption(label=result["original_title"], value=f"https://url-here//watch/movie/{result['id']}")
            for result in options
        ]

        self.select = discord.ui.Select(
            placeholder="Select a Movie",
            min_values=1,
            max_values=1,
            options=select_options,
            custom_id="movie_select"
        )
        self.select.callback = self.select_callback
        self.add_item(self.select)

    async def select_callback(self, interaction: discord.Interaction):
        view = Buttons()
        mvid = self.select.values[0].split('/')[-1]
        tmdb_url = f"https://api.themoviedb.org/3/movie/{mvid}"

        headers = {"accept": "application/json","Authorization": "API-Key Here"}
        response = requests.get(tmdb_url, headers=headers)
        if response.status_code != 200:
            return "response.status_code"

        response_data = response.json()
        overview = response_data.get("overview")
        title = response_data.get("title")
        thumbnail = response_data.get("poster_path")

        embed = discord.Embed(title=title, description=overview, color=discord.Color.blue())
        embed.set_thumbnail(url=f"https://image.tmdb.org/t/p/w300_and_h450_bestv2/{thumbnail}")
        embed.set_footer(text=f"© 2023 Trinix ™ | {title}", icon_url=f"https://image.tmdb.org/t/p/w300_and_h450_bestv2/{thumbnail}")
        view.add_item(discord.ui.Button(label="Watch Now",style=discord.ButtonStyle.link, url=self.select.values[0], emoji="▶️"))
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

class SelectTv(discord.ui.View):
    def __init__(self, options):
        super().__init__(timeout=None)
        select_options = [
            discord.SelectOption(label=result["original_name"], value=f"https://url-here/watch/tv/{result['id']}")
            for result in options
        ]

        self.select = discord.ui.Select(
            placeholder="Select a Tv Show",
            min_values=1,
            max_values=1,
            options=select_options,
            custom_id="movie_select"
        )
        self.select.callback = self.select_callback
        self.add_item(self.select)

    async def select_callback(self, interaction: discord.Interaction):
        view = Buttons()
        tvid = self.select.values[0].split('/')[-1]
        tmdb_url = f"https://api.themoviedb.org/3/tv/{tvid}"

        headers = {
            "accept": "application/json",
            "Authorization": "API-Key Here"
            }
        response = requests.get(tmdb_url, headers=headers)
        if response.status_code != 200:
            return "response.status_code"

        response_data = response.json()
        overview = response_data.get("overview")
        title = response_data.get("name")
        thumbnail = response_data.get("poster_path")

        embed = discord.Embed(title=title, description=overview, color=discord.Color.blue())
        embed.set_thumbnail(url=f"https://image.tmdb.org/t/p/w300_and_h450_bestv2/{thumbnail}")
        embed.set_footer(text=f"© 2023 Trinix ™ | {title}", icon_url=f"https://image.tmdb.org/t/p/w300_and_h450_bestv2/{thumbnail}")
        view.add_item(discord.ui.Button(label="Watch Now",style=discord.ButtonStyle.link, url=self.select.values[0], emoji="▶️"))
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

class Buttons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        pass
    
class Search(Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="Media Type (Tv | Movie)"))
        self.add_item(discord.ui.InputText(label="Search (please search for the exact name)"))

    async def callback(self, interaction: discord.Interaction):
        qu = self.children[1].value

        query = qu.replace(' ', '%20')

        url = f"https://api.themoviedb.org/3/search/{self.children[0].value.lower()}?query={query}"

        headers = {"accept": "application/json","Authorization": "API-Key Here"}
        
        response = requests.get(url, headers=headers).json()
        
        results = [result for result in response["results"]][:5]

        embed = discord.Embed(title=f"Top 5 Search Results", color=0x7289da)

        for i, result in enumerate(results):
            if self.children[0].value.lower() == "tv":
                title = result.get("original_name")
                media_type = SelectTv(results)
            else:
                title = result.get("original_title")
                media_type = SelectMovie(results)
            overview = result.get("overview")

            embed.add_field(name=f"{title}", value=f"**Overview:** {overview}", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1187754883303084159/1188395187253284964/3.png")
        await interaction.response.send_message(embed=embed, view=media_type)
        
class Movie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.update_list.start()

        self.movie_results = self.get_trending_movies()
        self.tv_results = self.get_trending_tv_shows()

        self.db_manager = DatabaseManager()

    def get_trending_movies(self):
        url = "https://api.themoviedb.org/3/trending/movie/day"

        headers = {"accept": "application/json","Authorization": "API-Key Here"}

        response = requests.get(url, headers=headers).json()
        results = [result for result in response["results"]][:5]

        return results

    def get_trending_tv_shows(self):
        url = "https://api.themoviedb.org/3/trending/tv/day?language=en-US"

        headers = {"accept": "application/json","Authorization": "API-Key Here"}

        response = requests.get(url, headers=headers).json()
        results = [result for result in response["results"]][:5]

        return results

    @tasks.loop(hours=1)
    async def update_list(self):
        channel = self.bot.get_channel(1188383059809153084)
        if channel:
            messages = await channel.history(limit=100).flatten()
            for message in messages:
                if message.embeds and message.embeds[0].footer and message.embeds[0].footer.text == "© 2023 Trinix ™ | Movie List":
                    embed = discord.Embed(title=f"Top 5 Trending Tv Shows", color=0x7289da)
                    results = self.tv_results
                    for i, result in enumerate(results):
                        title = result.get("name")
                        overview = result.get("overview")
                        embed.add_field(name=f"{title}", value=f"**Overview:** {overview}", inline=False)
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1187754883303084159/1188395187253284964/3.png")
                    embed.set_footer(text="© 2023 Trinix ™ | Tv Show List")
                    await message.edit(embed=embed, view=SelectTv(results))

    @commands.slash_command(description="Movie Search")
    async def search(self, ctx: discord.ApplicationContext):
        await ctx.send_modal(Search(title="Media Seach"))

    @commands.slash_command(description="Top 5 Trending Movies")
    async def trending_movies(self, ctx):
        await ctx.respond("Here are your results.", ephemeral=True)
        embed = discord.Embed(title=f"Top 5 Trending Movies", color=0x7289da)
        results = self.movie_results
        for i, result in enumerate(results):
            title = result.get("original_title")
            overview = result.get("overview")
            embed.add_field(name=f"{title}", value=f"**Overview:** {overview}", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1187754883303084159/1188395187253284964/3.png")
        embed.set_footer(text="© 2023 Trinix ™ | Movie List")
        await ctx.send(embed=embed, view=SelectMovie(results))

    @commands.slash_command(description="Top 5 Trending Tv Shows")
    async def trending_tv_shows(self, ctx):
        await ctx.respond("Here are your results.", ephemeral=True)
        embed = discord.Embed(title=f"Top 5 Trending Tv Shows", color=0x7289da)
        results = self.tv_results
        for i, result in enumerate(results):
            title = result.get("original_name")
            overview = result.get("overview")
            embed.add_field(name=f"{title}", value=f"**Overview:** {overview}", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1187754883303084159/1188395187253284964/3.png")
        embed.set_footer(text="© 2023 Trinix ™ | Tv Show List")
        await ctx.send(embed=embed, view=SelectTv(results))

def setup(bot):
    bot.add_cog(Movie(bot))
