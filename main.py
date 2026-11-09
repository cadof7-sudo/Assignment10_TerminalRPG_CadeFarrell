from auth import register, login
from game import Game
from database import initialize_database

def main():
    initialize_database()
    print("\n=== THE SHATTERED CROWN ===")
    print("A terminal RPG adventure\n")
    while True:
        print("1. Register\n2. Login\n3. Exit")
        choice = input("> ").strip()
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                Game(user["username"]).run()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
