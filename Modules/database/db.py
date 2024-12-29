import os, sqlite3

class DatabaseManager:
    def __init__(self):
        self.db_file = "./Modules/database/trinix.db" 
        self.conn = None
        self.cur = None
        self.create_connection()

    def create_connection(self):
        """Establishes a connection to the database and sets up the schema if the database is new."""
        if not os.path.exists(self.db_file):
            self.conn = sqlite3.connect(self.db_file)
            self.cur = self.conn.cursor()
            self.database_setup()
        else:
            self.conn = sqlite3.connect(self.db_file)
            self.cur = self.conn.cursor()
        self.conn.commit()

    def database_setup(self):
        """Sets up the database schema."""
        try:
            self.cur.execute("""CREATE TABLE IF NOT EXISTS auth (
                                id INTEGER PRIMARY KEY,
                                token VARCHAR(255),
                                owner_id VARCHAR(255));""")
            self.cur.execute("""CREATE TABLE IF NOT EXISTS config (
                                id INTEGER PRIMARY KEY,
                                guild_id VARCHAR(255),
                                webhook VARCHAR(255),
                                message_logger VARCHAR(255),
                                voice_logger VARCHAR(255),
                                join_detection VARCHAR(255));""")
            self.cur.execute("""CREATE TABLE IF NOT EXISTS blacklist (
                                id INTEGER PRIMARY KEY,
                                guild_id VARCHAR(255),
                                member VARCHAR(255));""")
            self.cur.execute("""CREATE TABLE IF NOT EXISTS youtube_notifications (
                                id INTEGER PRIMARY KEY,
                                guild_id VARCHAR(255),
                                discord_channel_id VARCHAR(255),
                                youtube_channel_id VARCHAR(255),
                                last_video_id VARCHAR(255));""")
        except sqlite3.Error as e:
            print(f"Error setting up the database: {e}")
            raise

    def execute_query(self, query, params=None):
        """Executes a write query with error handling and ensures the connection is closed."""
        try:
            self.conn = sqlite3.connect(self.db_file)
            c = self.conn.cursor()
            if params:
                c.execute(query, params)
            else:
                c.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
        finally:
            if self.conn:
                self.conn.close()

    def execute_read_all_query(self, query, params=None):
        """Executes a read query and fetches all results with error handling."""
        try:
            self.conn = sqlite3.connect(self.db_file)
            c = self.conn.cursor()
            if params:
                c.execute(query, params)
            else:
                c.execute(query)
            return c.fetchall()
        except sqlite3.Error as e:
            print(f"Error executing read query: {e}")
            return None
        finally:
            if self.conn:
                self.conn.close()

    def execute_read_one_query(self, query, params=None):
        """Executes a read query and fetches a single result with error handling."""
        try:
            self.conn = sqlite3.connect(self.db_file)
            c = self.conn.cursor()
            if params:
                c.execute(query, params)
            else:
                c.execute(query)
            return c.fetchone()
        except sqlite3.Error as e:
            print(f"Error executing read query: {e}")
            return None
        finally:
            if self.conn:
                self.conn.close()
