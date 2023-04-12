import sqlite3
import os
from lib.db import schema


class DataStore:
    def __init__(self, working_dir):
        self.conn = None
        self.working_dir = working_dir
        self.db_filename = "sqlite3.db"
        self.db_parent_dir = os.path.join(self.working_dir, "storage")
        self.path_to_db_file = os.path.join(self.db_parent_dir, self.db_filename)
        self.sub_folders = ["backgrounds", "characters", "items", "monsters", "players"]
        self.verify_db()
        self.verify_folders()

    def verify_db(self):
        if not os.path.isfile(self.path_to_db_file):
            print("  - Database not found; initializing.")
            try:
                if not os.path.exists(self.db_parent_dir):
                    os.mkdir(self.db_parent_dir)
                self.conn = sqlite3.connect(self.path_to_db_file)
                self.add_schema()
            except Exception as e:
                print("  - Failed to form database: {}.".format(self.path_to_db_file))
                print(e)
                print("exiting...")
                exit()

    def verify_folders(self):
        for sub_folder in self.sub_folders:
            if not os.path.exists(os.path.join(self.db_parent_dir, sub_folder)):
                print("  - Creating {} folder.".format(sub_folder))
                os.mkdir(os.path.join(self.db_parent_dir, sub_folder))

    def add_schema(self):
        cursor = self.conn.cursor()
        tables = [schema.create_table_background,
                  schema.create_table_character,
                  schema.create_table_item,
                  schema.create_table_monster,
                  schema.create_table_player]
        for table in tables:
            cursor.execute(table)
        self.conn.commit()

