
import sqlite3

db_name = 'my_database.db'

''' - Use a `SELECT` statement + call the `fetchall()` method to fetch the 
rows returned by SELECT statement!
Example: 
query_statement = 'SELECT * FROM table_name'
rows = cursor.fetchall() - For ALL rows
|- returns a list of tuples, each contains field values of a row!
row = cursor.fetchone() - For a single row (that u specify)
|- returns a single row as a tuple!
rows = cursor.fetchmany(size)
|- 'size' specifies the number of rows u want to fetch!
'''

def query_all_rows(conn, arg1, arg2, arg3, table):
    cursor = conn.cursor()
    try:
        cursor.execute(f'SELECT {arg1}, {arg2}, {arg3} FROM {table}')
        rows = cursor.fetchall()
        for row in rows:
            print(f"querying all rows, returning a tuple: {row}")
            # use row[2] to print all row's `arg3` & no longer in a tuple!
        return rows
    except sqlite3.Error as e:
        print(e)


# binfing variable's to a query w/ `?`
def get_table_by_id(conn, ID, arg1, table):
    cursor = conn.cursor()
    query_param_state = f'SELECT {arg1} FROM {table} WHERE id=?'
    try:
        cursor.execute(query_param_state, (ID,))
        row = cursor.fetchone()
        if row:
            print(f"querying (id row '{ID}', title '{arg1}'): {row}")
        return row
    except sqlite3.Error as e:
        print(e)


def query_some_rows(conn, arg1, arg2, table, size):
    cursor = conn.cursor()
    query_some_state = f'SELECT {arg1}, {arg2} FROM {table}'
    try:
        cursor.execute(query_some_state)
        rows = cursor.fetchmany(size)
        for row in rows:
            print(f"fetching 1 of {size} rows: {row}")
        return rows
    except sqlite3.Error as e:
        print(e)


def main():
    try:
        with sqlite3.connect(db_name) as conn:
            # QUERY data from the table!
            query_all_rows(conn, 'id', 'name', 'priority', 'tasks')
            get_table_by_id(conn, 1, 'name', 'tasks')
            query_some_rows(conn, 'name', 'end_date', 'tasks', 3)
    except sqlite3.Error as e:
        print(e)


if __name__ == '__main__':
    main()