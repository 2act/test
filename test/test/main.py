import sqlite3
import os
import sys

# 兼容 PyInstaller 打包路径
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

db_path = os.path.join(base_path, "data.db")

# 连接数据库并执行操作
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, name TEXT);")
cur.execute("INSERT INTO user (name) VALUES ('Hello Alist');")
conn.commit()

cur.execute("SELECT * FROM user;")
for row in cur.fetchall():
    print("Fetched row:", row)

conn.close()
