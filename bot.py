#Trinix was made by Maxim. Trinix is fully free and will be up 24/7 
#For anymore info just go to https://trinixbot.xyz
#If you need to contact me for any reason my discord is UnknownToska#8888
#This is just in case I ever open source this.
#Required Imports
from discord.ext import commands

import discord, cogs, json, re, os

#Config
with open("config.json", "r") as confjson:
	configData = json.load(confjson)

token = configData["Token"]
prefix = configData["Prefix"]

intents = discord.Intents.all()
intents.members = True
Trinix = commands.Bot(command_prefix=(prefix), help_command = None, intents = intents)

@Trinix.event
async def on_ready():
    await Trinix.change_presence(activity=discord.Activity(type = discord.ActivityType.playing, name = "type ,help"))#activity status
    print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    print('████████ ██████  ██ ███    ██ ██ ██   ██      ██    ███████')
    print('   ██    ██   ██ ██ ████   ██ ██  ██ ██      ███    ██     ')
    print('   ██    ██████  ██ ██ ██  ██ ██   ███        ██    ███████')
    print('   ██    ██   ██ ██ ██  ██ ██ ██  ██ ██       ██         ██')
    print('   ██    ██   ██ ██ ██   ████ ██ ██   ██      ██ ██ ███████')
    print('   Made by : Maxim Trinix is now up and ready to use!      ')
    print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')

#Cogs
for f in os.listdir("cogs"):
    if re.match(r".*\.py.swp", f):
        pass
    elif re.match(r".*\.py", f):
        Trinix.load_extension("cogs." + f.replace(".py", ""))

#Token
Trinix.run(token)#you put your bot token inside of config.json
