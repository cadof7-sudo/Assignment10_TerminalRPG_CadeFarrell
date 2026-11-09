import hashlib
from tinydb import Query
from database import get_db

def _hash(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def register():
    username = input("Choose a username: ").strip()
    password = input("Choose a password: ").strip()
    if len(username) < 3 or len(password) < 4:
        print("Username must be 3+ characters and password 4+ characters.")
        return
    db = get_db()
    accounts = db.table("accounts")
    if accounts.contains(Query().username == username):
        print("That username is already registered.")
    else:
        accounts.insert({"username": username, "password_hash": _hash(password)})
        print("Account created. You can now log in.")
    db.close()

def login():
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    db = get_db()
    rows = db.table("accounts").search(
        (Query().username == username) & (Query().password_hash == _hash(password))
    )
    db.close()
    if rows:
        print(f"Welcome back, {username}!")
        return rows[0]
    print("Login failed. Check your username and password.")
    return None
