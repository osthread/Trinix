from discord.ext import commands
from discord import Option

import discord, ollama, io, asyncio, httpx

chat_lock = asyncio.Lock()

queue = []

response = httpx.get("https://nekos.best/api/v2/endpoints")
endpoints = response.json()
actions = list(endpoints.keys())[:25]

class apis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def run_ollama_in_thread(prompt, model):
        response = ollama.generate(
            model=model,
            prompt=prompt,
            options={'max_tokens': 50, 'temperature': 0.2}
        )
        return response['response']
        
    @commands.slash_command(description="Interact with Trinix AI using your choice of AI models.")
    async def chat(self, 
                  ctx: discord.ApplicationContext, 
                  model: discord.Option(str, "Choose model", choices=["nemotron-mini", "llama3.2:latest"]),
                  query: discord.Option(str, "Ask something")):
        global queue
        user = ctx.author

        if user in queue:
            await ctx.respond(f"{user.mention}, you are already in the queue. Wait for your turn.", ephemeral=True)
            return

        queue.append(user)
        position = len(queue)

        await ctx.defer()

        message = await ctx.followup.send(f"{user.mention}, {position} in the queue. Please wait...")

        while queue.index(user) > 0:
            position = queue.index(user) + 1
            await message.edit(content=f"{user.mention}, You are {position} in queue. {len(queue) - 1} users ahead of you.")
            await asyncio.sleep(5)

        if model == "orca-mini:13b":
            author_icon_url = "https://ollama.com/public/ollama.png"
            author_url = "https://ollama.com/library/orca-mini"
        elif model == "llama3.2:latest":
            author_icon_url = "https://ollama.com/public/ollama.png"
            author_url = "https://ollama.com/library/llama3.2"
        else:
            author_icon_url = "https://download.logo.wine/logo/Nvidia/Nvidia-Logo.wine.png"
            author_url = "https://ollama.com/library/nemotron-mini"

        async with chat_lock:
            try:
                await message.edit(content=f"{user.mention}, No one in queue!\nNow generating the response with [{model}]({author_url})...")

                response = await asyncio.get_event_loop().run_in_executor(None, lambda: apis.run_ollama_in_thread(query, model))
                
                queue.remove(user)

                if len(response) > 2000:
                    with io.StringIO() as file:
                        file.write(response)
                        file.seek(0)
                        await ctx.followup.send(
                            content="The response was too long, so here's a file with the complete response:",
                            file=discord.File(file, filename="trinix_response.txt")
                        )
                    await message.delete()
                else:
                    title_response = await asyncio.get_event_loop().run_in_executor(None, lambda: apis.run_ollama_in_thread(f"Generate a concise title under 256 characters for: {query}", "llama3.2:latest"))

                    embed = discord.Embed(
                        title=title_response,
                        description=response,
                        color=0x7289da
                    )
                    embed.set_author(name=f"Model: {model}", icon_url=author_icon_url, url=author_url)
                    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1319528120205967401.png")
                    embed.set_footer(text="Powered By Ollama", icon_url="https://ollama.com/public/ollama.png")

                    await message.edit(embed=embed)

            except discord.NotFound:
                await ctx.followup.send(f"{user.mention}, I couldn't update your message. Please try again.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

    @commands.slash_command(description="Execute fun and interactive neko actions.")
    async def neko(self, ctx, action: Option(str, "Choose an action!", choices=actions), member: discord.Member = None):
        response = httpx.get(f"https://nekos.best/api/v2/{action}")
        data = response.json()
        embed = discord.Embed(color=0x7289da)
        if member == ctx.author or member is None:
            embed.set_author(name=f"{ctx.author.name} has used {action}")
        else:
            embed.set_author(name=f"{ctx.author.name} has used {action} on {member.name}")
        embed.set_image(url=(data["results"][0]["url"]))
        await ctx.respond(embed=embed)
    
    @commands.slash_command(description="Enjoy entertaining prompts like truth, dare, would you rather, never have I ever, or paranoia.")
    async def fun(self, ctx, arg: Option(str, "Fun commands", choices=["truth", "dare", "wyr", "nhie", "paranoia"])):
        response = httpx.get(url=f"https://api.truthordarebot.xyz/v1/{arg}")
        data = response.json()
        if arg == "truth":
            embed = discord.Embed(title="Trinix Truth", description=data["question"], color=0x7289da)
        elif arg == "dare":
            embed = discord.Embed(title="Trinix Dare", description=data["question"], color=0x7289da)
        elif arg == "wyr":
            embed = discord.Embed(title="Trinix Would You Rather", description=data["question"], color=0x7289da)
        elif arg == "nhie":
            embed = discord.Embed(title="Trinix Never Have I Ever", description=data["question"], color=0x7289da)
        elif arg == "paranoia":
            embed = discord.Embed(title="Trinix Paranoia", description=data["question"], color=0x7289da)
        else: 
            embed = discord.Embed(title="[Trinix Error System]", description="[ERROR] This isn't a command.", color=0xff0000)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(apis(bot))
