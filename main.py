from discord.ext import commands
from Modules.database.db import DatabaseManager

import os, sys, discord

class Trinix(commands.Bot):
    def __init__(self, owner_id, token):
        self.db_manager = DatabaseManager()
        intents = discord.Intents.all()
        intents.members = True
        super().__init__(command_prefix=">", help_command=None, intents=intents, owner_id=owner_id)
        self.token = token

    def main(self):
        try:
            cogs_directory = os.path.join(os.path.dirname(__file__), "Modules")
            if cogs_directory not in sys.path:
                sys.path.append(cogs_directory)

            for extension in os.listdir("./Modules/cogs"):
                if extension.endswith(".py") and "_" not in extension:
                    try:
                        self.load_extension(f'Modules.cogs.{extension[:-3]}')
                    except Exception as e:
                        print(f"Failed to load extension {extension}: {e}")
                else:
                    print(f"Ignored file: {extension}")
            
            self.run(self.token)
        except Exception as e:
            print(f"An error occurred: {e}")

def setup_bot():
    try:
        db_manager = DatabaseManager()

        owner_id = db_manager.execute_read_one_query("SELECT owner_id FROM auth")
        token = db_manager.execute_read_one_query("SELECT token FROM auth")

        if not owner_id or not token or not token[0]:
            token = input("Enter bot token: ")
            owner_id = input("Enter Owner ID: ")
            self.db_manager.execute_query("INSERT INTO auth (token, owner_id) VALUES (?, ?)", (bot_token, owner_id))
        
        bot = Trinix(owner_id=owner_id[0], token=token[0])
        bot.main()

    except Exception as e:
        print(f"Error in setup_bot: {e}")

if __name__ == "__main__":
    setup_bot()
