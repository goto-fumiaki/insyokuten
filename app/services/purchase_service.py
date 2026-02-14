from app.repositories.db import get_connection

def save_purchase(purchase_date, material_id, quantity, amount):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO purchases (
            purchase_date,
            material_id,
            quantity,
            amount
        )
        VALUES (?, ?, ?, ?)
    """, (
        purchase_date,
        material_id,
        quantity,
        amount
    ))

    conn.commit()
    conn.close()
