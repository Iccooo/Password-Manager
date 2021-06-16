import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS password (id INTEGER PRIMARY KEY, program text, password text, email text, info text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM password")
        rows = self.cur.fetchall()
        return rows

    def insert(self, program, password, email, info):
        self.cur.execute("INSERT INTO password VALUES (NULL, ?, ?, ?, ?)",
                         (program, password, email, info))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM password WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, program, password, email, info):
        self.cur.execute("UPDATE password SET program = ?, password = ?, email = ?, info = ? WHERE id = ?",
                         (program, password, email, info, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()



