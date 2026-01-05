import os
import psycopg2

def get_conn():
    """Neon(Postgres) に接続してコネクションを返す"""
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise RuntimeError("DATABASE_URL が未設定です (.env を確認)")
    return psycopg2.connect(db_url)

def create_record_table():#カラムがなければ作る
    """SQLiteの users テーブル相当を Postgres に作る"""
    conn = get_conn()
    cur = conn.cursor()

    # UUID生成用（1回だけ必要だけど、IF NOT EXISTS なら毎回呼んでもOK）
    cur.execute('create extension if not exists "pgcrypto";')

    cur.execute("""
    create table if not exists users (
      id uuid primary key default gen_random_uuid(),
      name text,
      weight integer,
      sets integer,
      reps integer,
      days integer,
      created_at timestamptz not null default now()
    );
    """)

    conn.commit()
    cur.close()
    conn.close()

def test_connection():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select now();")
    print("Neon OK:", cur.fetchone())
    cur.close()
    conn.close()
