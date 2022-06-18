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

    def get_prefix(client, message): ##first we define get_prefix
        with open('prefixes.json', 'r') as f: ##we open and read the prefixes.json, assuming it's in the same file
            prefixes = json.load(f) #load the json as prefixes
        return prefixes[str(message.guild.id)] #recieve the prefix for the guild id given

    intents = discord.Intents.all()
    intents.members = True
    Trinix = commands.Bot(command_prefix= (get_prefix), help_command = None, intents = intents)

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

    @Trinix.event
    async def on_guild_join(guild): #when the bot joins the guild
        with open('prefixes.json', 'r') as f: #read the prefix.json file
            prefixes = json.load(f) #load the json file

        prefixes[str(guild.id)] = '.'#default prefix

        with open('prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
            json.dump(prefixes, f, indent=4) #the indent is to make everything look a bit neater

    @Trinix.event
    async def on_guild_remove(guild): #when the bot is removed from the guild
        with open('prefixes.json', 'r') as f: #read the file
            prefixes = json.load(f)

        prefixes.pop(str(guild.id)) #find the guild.id that bot was removed from

        with open('prefixes.json', 'w') as f: #deletes the guild.id as well as its prefix
            json.dump(prefixes, f, indent=4)

    @Trinix.command(pass_context=True)
    @commands.has_permissions(administrator=True) #ensure that only administrators can use this command
    async def changeprefix(ctx, prefix): #command: bl!changeprefix ...
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('prefixes.json', 'w') as f: #writes the new prefix into the .json
            json.dump(prefixes, f, indent=4)

        await ctx.send(f'Prefix changed to: {prefix}') #confirms the prefix it's been changed to
    #next step completely optional: changes bot nickname to also have prefix in the nickname
        name=f'{prefix}BotBot'

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