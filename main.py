from Modules.database.db import DatabaseManager
from discord.ext import commands

import os, discord

class Trinix(commands.Bot):
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.bot = self.get_bot()

    def get_bot(self):
        intents = discord.Intents.all()
        intents.members = True
        owner_id = self.db_manager.execute_read_one_query("SELECT owner_id FROM auth")
        trinix = commands.Bot(command_prefix=">", help_command = None, intents = intents, owner_id = owner_id[0])
        return trinix

    def main(self):
        token = self.db_manager.execute_read_one_query("SELECT token FROM auth")

        for extension in os.listdir("cogs"):
            if "_" in extension:
                pass
            else:
                self.bot.load_extension(f'cogs.{extension[:-3]}')
    
        self.bot.run(token[0])

    def bot_login(self):
        token = self.db_manager.execute_read_one_query("SELECT token FROM auth")
        if token is None:
            bot_token = input("Enter bot token: ")
            owner_id = input("Enter Owner ID: ")
            self.db_manager.execute_query("INSERT INTO auth (token, owner_id) VALUES (?, ?)", (bot_token, owner_id))
        else:
            self.main()

if __name__ == "__main__":
    run = Trinix()
    run.bot_login()
