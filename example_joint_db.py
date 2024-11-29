

import sqlite3

db_name = 'geometry_database_001.db'

def add_joint_table(conn):
    sql_joint_statements = [
    """ CREATE TABLE IF NOT EXISTS joints (
            id INTEGER PRIMARY KEY,
            type text NOT NULL,
            name text NOT NULL,
            side text NOT NULL
        );""",

    """ CREATE TABLE IF NOT EXISTS geometry (
            id INTEGER PRIMARY KEY,
            file_name text NOT NULL,
            file_ver INT,
            obj_id text NOT NULL
        );"""
    ]

    cur = conn.cursor()
    
    for table_state in sql_joint_statements:
        cur.execute(table_state)

    conn.commit()


def add_joints_row(conn, table):    
    sql = ''' INSERT INTO joints (type,name,side)
              VALUES(?,?,?)'''
    
    cur = conn.cursor()

    cur.execute(sql, table)

    conn.commit()

    return cur.lastrowid


def add_geometry_row(conn, data):

    sql = ''' INSERT INTO geometry (file_name,file_ver,obj_id)
              VALUES(?,?,?)'''
    
    cur = conn.cursor()

    cur.execute(sql, data)

    conn.commit()

    return cur.lastrowid


def main():
    try:
        with sqlite3.connect(db_name) as conn:
            # Create the table
            add_joint_table(conn)

            geometry = [
                ("robot_high", "OO1", "DF346BE5-4545-5AB0-EDA9-90A0B2BB8B40"),
                ("robot_block", "OO3", "BDD73728-4ABC-A170-AB94-C5809CD09EF2"),
                ("robot_block", "OO3", "5C35E7EE-44A3-6570-0A36-4791C63AF4BA")
            ]
            for geo in geometry:
                geo_id = add_geometry_row(conn, geo)
                print(f"created a geometry row with the id {geo_id}")

            joints = [
                ("rig", "hip", "L"),
                ("skn", "wrist", "R"),
                ("skn", "spine_01", "M")
            ]
            
            for jnts in joints:
                jnt_id = add_joints_row(conn, jnts)
                print(f"created a joint row with the id {jnt_id}")


    except sqlite3.Error as e:
        print(e)

if __name__ == '__main__':
    main()

