import sqlite3
import os


class DataStore:
    def __init__(self, working_dir):
        self.conn = None
        self.working_dir = working_dir
        self.db_filename = "sqlite3.db"
        self.path_to_db = os.path.join(self.working_dir, "data", self.db_filename)
        if not os.path.isfile(self.path_to_db):
            self.create_db()

    def create_db(self):
        print("  - Creating sqlite3 database.")
        try:
            self.conn = sqlite3.connect(self.path_to_db)
            print("  - Formed database:  {}.".format(self.path_to_db))
        except Exception as e:
            print("Failed to form database: {}.".format(self.path_to_db))
            print(e)

