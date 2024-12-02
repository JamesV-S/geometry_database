
import sqlite3

db_name = 'my_database.db'

# after connecting the database, create cursor() object.
# Use an INSERT statement that inserts a row in the table. 
# then commit() it

# -------------a
# to [pass arguments] to the insert statement, use [ ? ] as  the placeholder for each
'''
INSERT INTO table_name(c1, c2)
VALUES(?,?)
'''
# ^ 'c1' & 'c2' are collumns of the table 'table_name'. the '?' are placeholders for the 'c1' & 'c2'

# define a function that inserts a new row into the projects table:
def add_project(conn, project):
    # insert table statement
    sql = ''' INSERT INTO projects (name,begin_date,end_date)
              VALUES(?,?,?)'''
    
    # Create a cursor > allows me to execute SQL commands and quieries, 
    # cus it acts as an intermediary between python & the database.
    cur = conn.cursor()

    # execute the INSERT statement
    cur.execute(sql, project)

    # commit the changes
    conn.commit()

    # get the id of the last inserted row
    return cur.lastrowid


def add_task(conn, task):
    # insert table statement
    sql = ''' INSERT INTO tasks (name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?)'''
    
    cur = conn.cursor()

    cur.execute(sql, task)

    conn.commit()

    return cur.lastrowid


def main():
    try:
        with sqlite3.connect(db_name) as conn:
            # add a project
            project = ("Cool App with SQLite & Python", "2015-01-01", "2015-01-30")
            project_id = add_project(conn, project)
            print(f"created a project with the id {project_id}")

            # add tasks to the project
            tasks = [
                ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02'),
                ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')
            ]

            for tsk in tasks:
                task_id = add_task(conn, tsk)
                print(f"created a task with the id {task_id}")


    except sqlite3.Error as e:
        print(e)

if __name__ == '__main__':
    main()


