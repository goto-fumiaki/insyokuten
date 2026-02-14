import sqlite3

conn = sqlite3.connect("inventory.db")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

rows = cur.execute("""
    SELECT
        p.id,
        p.purchase_date,
        m.name AS material_name,
        p.quantity,
        p.amount
    FROM purchases p
    JOIN materials m ON p.material_id = m.id
    ORDER BY p.id
""").fetchall()

print(f"purchases 件数: {len(rows)}")
for r in rows:
    print(
        r["id"],
        r["purchase_date"],
        r["material_name"],
        r["quantity"],
        r["amount"]
    )

conn.close()
