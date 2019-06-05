import sqlite3

conn = sqlite3.connect("my_friends.db")

c = conn.cursor()
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")

data = ("Steve", "Irwin", 9)
query = "INSERT INTO friends VALUES (?,?,?)"
c.execute(query, data)

conn.commit()
conn.close()
