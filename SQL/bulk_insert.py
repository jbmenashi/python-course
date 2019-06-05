import sqlite3
conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()

people = [
	("Roald", "Amundsen", 5),
	("Rosa", "Parks", 8),
	("Henry", "Hudson", 7),
	("Neil", "Armstrong", 7),
	("Daniel", "Boone", 3)]

# insert one at a time
for person in people:
	c.execute("INSERT INTO friends VALUES (?,?,?)", person)

# Insert all at once
c.executemany("INSERT INTO friends VALUES (?,?,?)", people)

# commit changes
conn.commit()
conn.close()
