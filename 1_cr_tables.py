
import sqlite3

db_name = 'my_database.db'

# define a list that stores the 'create_table' statements
sql_cr_table_statements = [
    """ CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY,
            name text NOT NULL,
            begin_date DATE,
            end_date DATE
        );""",

    """ CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name text NOT NULL,
            priority INT,
            project_id INT NOT NULL,
            status_id INT NOT NULL,
            begin_date DATE NOT NULL,
            end_date DATE NOT NULL,
            FOREIGN KEY (project_id) REFERENCES projects (id)
        );"""
]

# if the db alr exists, it'll open a connection to that db.
try:
    with sqlite3.connect(db_name) as conn:
        print(f"Opened SQLite database [{db_name}] with version {sqlite3.sqlite_version} successfully.")
        # cr a cursor object with [cursor()] method of connection object
        cursor = conn.cursor()

        # pass the [""" table (); """] statement list to the [execute()] method of connection object
        # iterate over & execute statements
        for statement in sql_cr_table_statements:
            cursor.execute(statement)

        # apply the changes to the db by calling the [commit()] function
        conn.commit()
        print("Tables created successfully.")
        
except sqlite3.OperationalError as e:
    print(f"database [{db_name}] opertionalError: {e}")


