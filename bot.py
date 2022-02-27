#Trinix was made by Maxim. Trinix is fully free and will be up 24/7 
#for anymore info just go to https://trinixbot.xyz
#If you need to contact me for any reason my discord is UnknownToska#8888
#This is just in case I ever open source this.
#Required Imports
import os
import re
import json
import cogs
import discord
from discord.ext import commands

#Config
if os.path.exists (os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"Token": "", "Prefix": "", "Owner": ""}
    with open(os.getcwd() +"/config.json", "w+") as f:json.dump (configTemplate, f)

token = configData["Token"]
prefix = configData["Prefix"]
owner = configData["Owner"]

client = commands.Bot(
        command_prefix = commands.when_mentioned_or(prefix),#Bot prefix if you wanna chnage this just go into config.json
        help_command = None #Help category. I disabled this because i am using a custom help
)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type = discord.ActivityType.playing, name = ".help for commands | Maxie is my master <3"))#activity status
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
        client.load_extension("cogs." + f.replace(".py", ""))
        
#Token
client.run(token)#you put your bot token inside of config.json
