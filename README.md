# Login Attempt Control System

A Python program that limits repeated incorrect password attempts and temporarily locks access after too many failures.

## Features

- User registration and login
- Passwords are stored as salted hashes (never plain text)
- Allows only 3 incorrect attempts
- Locks the account for 30 seconds after the limit is reached
- Shows remaining attempts and lock time

## How to Run

```
python login_system.py
```

Register a user first, then try logging in with a wrong password 3 times to see the lockout.

## How It Works

1. Each failed login increases a counter for that user.
2. When the counter reaches the limit, the account is locked for a fixed time.
3. A successful login resets the counter.

This shows how systems prevent brute-force and unauthorized access.

## Author

Pron1302
