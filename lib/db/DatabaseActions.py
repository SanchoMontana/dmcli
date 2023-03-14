import os
import sqlite3

class DB:
    def __init__(self, working_dir):
        self.filename = os.path.join(working_dir, "storage", "sqlite3.db")
        
        self.conn = sqlite3.connect(self.filename) # Connection to the on-disk database.
        self.cur = self.conn.cursor()

    def get_table_objects(self, table):
        results = self.cur.execute("SELECT * FROM {}".format(table))
        return results.fetchall()
    
    def add_table_object(self, table, **kwargs):
        print(table)
        key_vals = list(kwargs.items())
        key_vals.sort()
        base = "INSERT INTO {}({})".format(table, key_vals)
        print(base)
        return

    def remove_table_object(self, table, **kwargs):
        db_cmd = "DELETE FROM {} ".format(table)
        search_condition = None
        if kwargs:
            search_condition = "WHERE "
            for k, v in kwargs.items():
                search_condition += "{} = {}".format(k, v)
        db_cmd += search_condition
        print(db_cmd)
        ret = self.conn.execute(db_cmd)
        return ret
