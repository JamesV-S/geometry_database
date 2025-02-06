
import sqlite3

db_name = 'my_database.db'

''' - To  bind arguments to the `UPDATE` statement, use `?` for each argument:
*update_datement* = UPDATE table_name SET column1=?, column2=? WHERE id = ?
'''
# construct an update statement:
table = 'tasks'
update_statement = f'UPDATE {table} SET priority = ?, status_id = ? WHERE id = ?'
date_update_state = f'UPDATE {table} SET end_date = ?'
name_update_state = f'UPDATE {table} SET name = ? WHERE id = ?'

def update_specififc_data(conn, sql, arg1, arg2, ID):
    cursor = conn.cursor()
    try:
        # execute the UPDATE statement with the priority and id.
        cursor.execute(f"SELECT * FROM {table} WHERE id = ?", (ID,))
        if cursor.fetchone() is None:
            print(f"No task found with id: `{ID}`.")
            return
        
        # Execute the UPDATE statement
        cursor.execute(sql, (arg1, arg2, ID))
        conn.commit()
        if cursor.rowcount == 0:
            print(f"No '{table}' table found with id `{ID}`.")
        else:
            print(f"'{table}' table found with id `{ID}`.")

        # verify the update on a specific row: 
        cursor.execute('SELECT id, priority, status_id FROM tasks WHERE id = ?', (ID,))
        row = cursor.fetchone() # Gets all rows from the result of the query
        if row: 
            print("Verifying the update:")
            print(row)
        else:
            print(f"No '{table}' table found with id `{ID}`.")

    except sqlite3.Error as e:
        print(f"An error occured in the UPDATE statement: {e}")
update_specififc_data(conn, update_statement, 58, 52, 2)


# With no ID specified the update is applied to ALL rows
def update_all_columns_dates(conn, sql, arg1): 
    cursor = conn.cursor()
    try:
        # Execute the UPDATE statement
        cursor.execute(sql, (arg1,) )
        conn.commit()

        # print a query result of the updates made on ALL rows: 
        cursor.execute('SELECT id, name, end_date FROM tasks')
        rows = cursor.fetchall() # Gets all rows from the result of the query
        print("Verifying the date update:")
        for row in rows:
            print(row)
    
    except sqlite3.Error as e:
        print(f"An error occured in the 'date' UPDATE statement: {e}") 

def update_name(conn, sql, arg1, ID):
    cursor = conn.cursor()
    try:
        # Execute the UPDATE statement
        cursor.execute(sql, (arg1, ID))
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occured in the 'name' UPDATE statement: {e}") 

def main():
    try:
        with sqlite3.connect(db_name) as conn:
            # UPDATE one field of one row in the table!
            '''
            update_specififc_data(conn, update_statement, 58, 52, 2)
            update_all_columns_dates(conn, date_update_state, '2004-03-10')
            '''
            update_name(conn, name_update_state, 'App_analysis_requirements', 1)
            update_name(conn, name_update_state, 'Top_requirments_confirmation', 2)
    except sqlite3.Error as e:
        print(e)


if __name__ == '__main__':
    main()
