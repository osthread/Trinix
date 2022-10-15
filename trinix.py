# Trinix Rewrite (10/3/2022)
# This will be fully open-source and will be free to use.
# If you use Trinix you must give me some credit.
# If need be make a support ticket on my discord https://discord.gg/eDpPP5BXyf/
# 
# Features
# - Neko Commands
# - Community Commands
# - Error listener
# - Anti Nuke (Updating)
# - Music Commands (Updating)
# - Mod Automation (Updating)
# - Admin Commands (Updating)

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
    Trinix = commands.Bot(command_prefix=configData["Prefix"], help_command = None, intents = intents)# Prefix is inside of config.json

    @Trinix.event
    async def on_ready():# Will show any errors if any
        await Trinix.change_presence(activity=discord.Activity(type = discord.ActivityType.listening, name = "Maxie | .help cmd"))# Activity Atatus
        print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
        print('         ████████ ██████  ██ ███    ██ ██ ██   ██          ')
        print('            ██    ██   ██ ██ ████   ██ ██  ██ ██           ')
        print('            ██    ██████  ██ ██ ██  ██ ██   ███            ')
        print('            ██    ██   ██ ██ ██  ██ ██ ██  ██ ██           ')
        print('            ██    ██   ██ ██ ██   ████ ██ ██   ██          ')
        print('            Trinix is now up and ready to use!             ')
        print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')

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

    Trinix.run(configData["Token"])# Put your token inside of config.json

if __name__=="__main__":
    main()

# --------------------------------------------------------------------------------------------------------------------------------
