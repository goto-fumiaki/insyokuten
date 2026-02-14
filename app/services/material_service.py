from app.repositories.db import get_connection

def get_materials():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, name, unit
        FROM materials
        WHERE is_active = 1
        ORDER BY name
    """)

    rows = cur.fetchall()
    conn.close()
    return rows
