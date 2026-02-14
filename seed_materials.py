import sqlite3

conn = sqlite3.connect("inventory.db")
cur = conn.cursor()

cur.execute("""
INSERT INTO materials (name, unit)
VALUES (?, ?)
""", ("鶏もも肉", "kg"))

conn.commit()
conn.close()

print("material inserted")
