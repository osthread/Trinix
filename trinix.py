#Trinix was made by Maxim. Trinix is fully free and will be up 24/7
#If you need to contact me for any reason my discord is Maxie#0008
#This is just in case I ever open source this.

# ---------------------------------------------------------------- Required Imports ----------------------------------------------------------------

from discord.ext import commands

import discord, re, json, os, traceback, sys

# ---------------------------------------------------------------- Config ----------------------------------------------------------------

with open("config.json", "r") as confjson:
	configData = json.load(confjson)

# ---------------------------------------------------------------- Trinix ----------------------------------------------------------------

def main():

    intents = discord.Intents.all()
    intents.members = True
    Trinix = commands.Bot(command_prefix=configData["Token"], help_command = None, intents = intents)

    @Trinix.event
    async def on_ready():#This shows when the bot is online and working
        await Trinix.change_presence(activity=discord.Activity(type = discord.ActivityType.listening, name = "Maxie | .h cmd"))#activity status
        print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
        print('████████ ██████  ██ ███    ██ ██ ██   ██      ██    ███████')
        print('   ██    ██   ██ ██ ████   ██ ██  ██ ██      ███    ██     ')
        print('   ██    ██████  ██ ██ ██  ██ ██   ███        ██    ███████')
        print('   ██    ██   ██ ██ ██  ██ ██ ██  ██ ██       ██         ██')
        print('   ██    ██   ██ ██ ██   ████ ██ ██   ██      ██ ██ ███████')
        print('   Made by : Maxim Trinix is now up and ready to use!      ')
        print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')

    #Cogs
    FileNameLst = os.listdir("cogs")
    for extension in FileNameLst:
        try:
            if "_" in extension:
                pass
            else:
                Trinix.load_extension(f'cogs.{extension[:-3]}')
        except Exception as e:
            print(f'Failed to load extension {extension[:-3]}.', file=sys.stderr)
            traceback.print_exc()

    #Token
    Trinix.run(configData["Token"])#you put your bot token inside of config.json

if __name__=="__main__":
    main()

# --------------------------------------------------------------------------------------------------------------------------------