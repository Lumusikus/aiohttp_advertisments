import aiosqlite
import asyncio

DB_NAME = "advertisements.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS advertisements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                created_at TEXT NOT NULL,
                owner TEXT NOT NULL
            )
        """)
        await db.commit()

async def create_ad(title: str, description: str, owner: str):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "INSERT INTO advertisements (title, description, created_at, owner) VALUES (?, ?, datetime('now'), ?)",
            (title, description, owner)
        )
        await db.commit()
        return cursor.lastrowid

async def get_ad(ad_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT * FROM advertisements WHERE id = ?", (ad_id,))
        row = await cursor.fetchone()
        return row

async def get_all_ads():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT * FROM advertisements")
        rows = await cursor.fetchall()
        return rows

async def update_ad(ad_id: int, title: str, description: str, owner: str):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "UPDATE advertisements SET title = ?, description = ?, owner = ? WHERE id = ?",
            (title, description, owner, ad_id)
        )
        await db.commit()

async def delete_ad(ad_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("DELETE FROM advertisements WHERE id = ?", (ad_id,))
        await db.commit()
