
import sqlite3

db_name = 'my_database.db'

'''- Executing a delete statement
sqp_del_state = 'DELETE FROM table_name WHERE id = ?'
- In this case, u must pass the second arg as a tuple including the id to the 
    exeute method:
cursor.execute(sqp_del_state, (id,))
'''

table_name = "temp_tbl"
cr_temp_table = '''CREATE TABLE IF NOT EXISTS temp_tbl (
                id INTEGER PRIMARY KEY, 
                Name text NOT NULL,
                Uni text NOT NULL,
                Course text NOT NULL, 
                Year INT
                )'''
# add a new temp row to then delete it as a test:
temp_add_row_state = f"INSERT INTO {table_name} (Name,Uni,Course,Year) VALUES(?, ?, ?, ?)"
temp_del_row_state = f"DELETE FROM {table_name} WHERE id=?"
    
def add_temp_table(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    # return 

def add_temp_row(conn, sql, arg):
    cursor = conn.cursor()
    # execute the INSERT statement
    cursor.execute(sql, arg)
    # commit the changes
    conn.commit()
    # get the id of the last inserted row
    return cursor.lastrowid

def del_temp_row(conn, sql, arg):
    cursor = conn.cursor()
    cursor.execute(sql, arg)

def main():
    try:
        with sqlite3.connect(db_name) as conn:
            # Create a temp table.
            #add_temp_table(conn, cr_temp_table)
            # Insert a temporary row.
            args = [
                ('Lilirose_Kent', 'Oxford', 'History', 2),
                ('James_Vilela-Slater', 'Hertfordshire', 'VFX', 3)
            ]
            #for arg in args:
            #    temp_id = add_temp_row(conn, temp_add_row_state, arg)
            #    print(f"added a row with the id {temp_id}")
            
            # Delete that row.
            del_temp_row(conn, temp_del_row_state, (1,))

    except sqlite3.Error as e:
        print(f"sqlite3.Error: {e}")


if __name__ == '__main__':
    main()
