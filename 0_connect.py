
import sqlite3

# Creates a new database in the same directory as this file called "my_database"
try:
    with sqlite3.connect("my_database.db") as conn:
        print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")
        # Interact with database
        
except sqlite3.OperationalError as e:
    print(f"failed to open database: {e}")

''' creates the database in memory using ':memory:'
import sqlite3

try:
    with sqlite3.connect(':memory:') as conn:
        # interact with database
        pass
except sqlite3.OperationalError as e:
    print("Failed to open database:", e)
'''