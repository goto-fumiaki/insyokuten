import sqlite3

conn = sqlite3.connect("inventory.db")
cur = conn.cursor()

# materials
cur.execute("""
CREATE TABLE IF NOT EXISTS materials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    unit TEXT NOT NULL,
    is_active INTEGER DEFAULT 1
);
""")

# purchases（★金額対応・最終確定）
cur.execute("""
CREATE TABLE IF NOT EXISTS purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    purchase_date TEXT NOT NULL,
    material_id INTEGER NOT NULL,
    quantity REAL NOT NULL,
    amount INTEGER NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (material_id) REFERENCES materials(id)
);
""")

conn.commit()
conn.close()

print("DB initialized")
