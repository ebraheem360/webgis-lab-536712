import sqlite3
import os

db_path = os.path.expanduser(r"~\AppData\Roaming\pgAdmin\pgadmin4.db")
con = sqlite3.connect(db_path)
cur = con.cursor()

tables = [r[0] for r in cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()]
print("Tables:", tables)

if "server" in tables:
    for row in cur.execute("SELECT id, name, host, port, username, password FROM server").fetchall():
        print("Server:", row)
