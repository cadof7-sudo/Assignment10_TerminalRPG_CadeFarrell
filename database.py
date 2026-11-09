from tinydb import TinyDB

DB_FILE = "rpg_data.json"

def get_db():
    return TinyDB(DB_FILE)

def initialize_database():
    db = get_db()
    db.table("accounts")
    db.table("saves")
    db.close()

def load_save(username):
    db = get_db()
    rows = db.table("saves").search(lambda row: row.get("username") == username)
    save = rows[0] if rows else None
    db.close()
    return save

def save_game(username, data):
    db = get_db()
    table = db.table("saves")
    table.upsert({"username": username, **data}, lambda row: row.get("username") == username)
    db.close()
