import sqlite3
with open("shop_db.sql", encoding="utf-8") as f:
    sql = f.read()
db = sqlite3.connect("shop.db")
db.executescript(sql)
db.close
print("done")