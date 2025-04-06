import sqlite3

DB='record.db'

def create_record_table():
    conn = sqlite3.connect(DB)  
    con = conn.cursor()
    con.execute("""
    CREATE TABLE IF NOT EXISTS users (
    name TEXT ,
    weight INTEGER,
    sets INTEGER,
    reps INTEGER,
    days INTEGER,
    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    con.close()