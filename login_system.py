import time
import hashlib
import os
import getpass

MAX_ATTEMPTS = 3
LOCK_SECONDS = 30

users = {}      # username -> (salt, password_hash)
failed = {}     # username -> number of failed attempts
locked_until = {}  # username -> unlock time


def hash_password(password, salt):
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100_000)


def register():
    username = input("Choose a username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return
    if username in users:
        print("Username already exists.")
        return
    password = getpass.getpass("Choose a password: ")
    if len(password) < 4:
        print("Password must be at least 4 characters.")
        return
    salt = os.urandom(16)
    users[username] = (salt, hash_password(password, salt))
    print("Registration successful!")


def login():
    username = input("Username: ").strip()
    if username not in users:
        print("User not found.")
        return

    # Check if account is locked
    remaining = locked_until.get(username, 0) - time.time()
    if remaining > 0:
        print(f"Account locked. Try again in {int(remaining) + 1} seconds.")
        return

    password = getpass.getpass("Password: ")
    salt, stored = users[username]

    if hash_password(password, salt) == stored:
        print(f"Login successful. Welcome, {username}!")
        failed[username] = 0
        locked_until.pop(username, None)
    else:
        failed[username] = failed.get(username, 0) + 1
        left = MAX_ATTEMPTS - failed[username]
        if left <= 0:
            locked_until[username] = time.time() + LOCK_SECONDS
            failed[username] = 0
            print(f"Too many failed attempts. Account locked for {LOCK_SECONDS} seconds.")
        else:
            print(f"Incorrect password. {left} attempt(s) left.")


def main():
    print("=== Login Attempt Control System ===")
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
