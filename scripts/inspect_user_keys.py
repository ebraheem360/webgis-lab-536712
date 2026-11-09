import sqlite3
import os

db_path = os.path.expanduser(r"~\AppData\Roaming\pgAdmin\pgadmin4.db")
con = sqlite3.connect(db_path)
cur = con.cursor()

for row in cur.execute("SELECT * FROM user").fetchall():
    print("User:", row)

for row in cur.execute("SELECT * FROM keys").fetchall():
    print("Keys:", row)
