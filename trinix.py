#Trinix was made by Maxim. Trinix is fully free and will be up 24/7
#If you need to contact me for any reason my discord is Maxie#0008
#This is just in case I ever open source this.

# ---------------------------------------------------------------- Required Imports ----------------------------------------------------------------

from discord.ext import commands

import discord, re, json, os

# ---------------------------------------------------------------- Config ----------------------------------------------------------------

with open("config.json", "r") as confjson:
	configData = json.load(confjson)

# ---------------------------------------------------------------- Trinix ----------------------------------------------------------------

def main():

    intents = discord.Intents.all()
    intents.members = True
    Trinix = commands.Bot(command_prefix=(configData["Prefix"]), help_command = None, intents = intents)

    @Trinix.event
    async def on_ready():#This shows when the bot is online and working
        await Trinix.change_presence(activity=discord.Activity(type = discord.ActivityType.listening, name = "Maxie | .h cmd"))#activity status
        print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
        print('████████ ██████  ██ ███    ██ ██ ██   ██      ██    ███████')
        print('   ██    ██   ██ ██ ████   ██ ██  ██ ██      ███    ██     ')
        print('   ██    ██████  ██ ██ ██  ██ ██   ███        ██    ███████')
        print('   ██    ██   ██ ██ ██  ██ ██ ██  ██ ██       ██         ██')
        print('   ██    ██   ██ ██ ██   ████ ██ ██   ██      ██ ██ ███████')
        print('   Made by : Maxie Trinix is now up and ready to use!      ')
        print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')

    #Cogs
    for f in os.listdir("cogs"):
        if re.match(r".*\.py.swp", f):
            pass
        elif re.match(r".*\.py", f):
            Trinix.load_extension("cogs." + f.replace(".py", ""))

    #Token
    Trinix.run(configData["Token"])#you put your bot token inside of config.json

if __name__=="__main__":
    main()

# --------------------------------------------------------------------------------------------------------------------------------