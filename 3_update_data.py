
import sqlite3

db_name = 'my_database.db'

# - To  bind arguments to the `UPDATE` statement, use `?` for each argument:
# UPDATE table_name SET column1=?, column2=? WHERE id = ?

# construct an update statement: 
update_statement = 'UPDATE tasks SET priority = ?, status_id = ? WHERE id = ?'

def update_data(conn, sql, arg1, arg2, id_):
    cursor = conn.cursor()
    try:
        # execute the UPDATE statement with the priority and id. 
        cursor.execute(sql, (arg1, arg2, id_))
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occured in the UPDATE statement: {e}") 

def main():
    try:
        with sqlite3.connect(db_name) as conn:
            # UPDATE one field of one row in the table!
            update_data(conn, update_statement)

    except sqlite3.Error as e:
        print(e)


if __name__ == '__main__':
    main()
