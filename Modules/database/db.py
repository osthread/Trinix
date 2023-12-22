import os, sqlite3

class DatabaseManager:
    def __init__(self):
        self.db_file = "Set-Database_Path-Here" 
        self.conn = None
        self.cur = None
        self.create_connection()

    def create_connection(self):
        if not os.path.exists(self.db_file):
            self.conn = sqlite3.connect(self.db_file)
            self.cur = self.conn.cursor()
            self.database_setup()
        else:
            self.conn = sqlite3.connect(self.db_file)
            self.cur = self.conn.cursor()

    def database_setup(self):
        try:
            self.cur.execute("""CREATE TABLE IF NOT EXISTS auth(id INTEGER PRIMARY KEY,token VARCHAR(255),owner_id VARCHAR(255));""")
            self.cur.execute("""CREATE TABLE IF NOT EXISTS config(id INTEGER PRIMARY KEY,guild_id VARCHAR(255),webhook VARCHAR(255),message_logger VARCHAR(255),voice_logger VARCHAR(255),join_detection VARCHAR(255));""")
            self.cur.execute("""CREATE TABLE IF NOT EXISTS blacklist(id INTEGER PRIMARY KEY,guild_id VARCHAR(255),member VARCHAR(255));""")
            row = self.cur.fetchone()
            if row is None:
                self.cur.execute("""INSERT INTO auth (token,owner_id) VALUES ('Token-Here', 'Owner-ID-HERE');""") # Set both token and owner id here
            self.conn.commit()
        except sqlite3.Error as e:
            return f"Error setting up the database: {e}"

    def execute_query(self, query, params = None):
        c = self.conn.cursor()
        if params:
            c.execute(query, params)
        else:
            c.execute(query)
        self.conn.commit()

    def execute_read_all_query(self, query, params = None):
        c = self.conn.cursor()
        if params:
            c.execute(query, params)
        else:
            c.execute(query)
        return c.fetchall()

    def execute_read_one_query(self, query, params = None):
        c = self.conn.cursor()
        if params:
            c.execute(query, params)
        else:
            c.execute(query)
        return c.fetchone()
