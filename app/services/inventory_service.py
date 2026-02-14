from app.repositories.db import get_connection

def save_inventory(inventory_date, material_id, actual_quantity):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO inventories (
            inventory_date,
            material_id,
            actual_quantity
        )
        VALUES (?, ?, ?)
    """, (
        inventory_date,
        material_id,
        actual_quantity
    ))

    conn.commit()
    conn.close()
