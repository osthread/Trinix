from Modules.database.db import DatabaseManager
from Modules.error.logger import CustomLogger
from discord.ext import commands

import os, sys, logging, discord, traceback

class Trinix(commands.Bot):
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.custom_logger = CustomLogger('Main', log_level=logging.INFO)
        self.logger = self.custom_logger.get_logger()
        self.token = self.get_token()
        self.bot = self.get_bot()

    def get_token(self):
        token = self.db_manager.execute_read_one_query("SELECT token FROM auth")
        return token[0]

    def get_bot(self):
        intents = discord.Intents.all()
        intents.members = True
        trinix = commands.Bot(command_prefix=">", help_command = None, intents = intents, owner_id = 1028543893383421954)
        return trinix

    def main(self):
        for extension in os.listdir("cogs"):
            if "_" in extension:
                pass
            else:
                self.bot.load_extension(f'cogs.{extension[:-3]}')
    
        self.bot.run(self.token)

    def bot_login(self):
        token = self.db_manager.execute_read_one_query("SELECT token FROM auth")
        if token is None:
            bot_token = input("Enter bot token: ")
            owner_id = input("Enter Owner ID: ")
        else:
            self.main()

if __name__ == "__main__":
    run = Trinix()
    run.bot_login()
