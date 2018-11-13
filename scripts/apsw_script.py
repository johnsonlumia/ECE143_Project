#
# Another Python Sqlite Wrapper script file
# 
# create functions that uses apsw package for project use
#
# by Renjie Zhu on Nov 4, 2018
#

import apsw

def connect_db(db_name):
    """
    establish a coonnection with a database with the given name

    arguments
    ---------

    db_name: the name of the database
        type: string
    
    return
    ------
    
    connection to the database
        type: apsw.Connection()
    
    cursor of the database
        type: apsw.cursor
    """
    
    connection = apsw.Connection(db_name)
    cursor = connection.cursor()

    return connection, cursor


def create_table(cursor, table_name):
    """
    create a table in SQLite with a name

    the table will be structured like following

    word: tinystr
    
    freq: int

    arguments
    ---------

    cursor: the cursor used to communiate with the database
        type: apsw.cursor

    table_name: the name of the table
        type: string
        naming convention: school_dept_year
    
    return
    ------
    
    error code
        type: int
        0: no errors
        1: error occurs (table exist)

    ...

    """
    
    table_create = "CREATE TABLE " + table_name + "(word TINYTEXT, freq INT)"
    
    try:
        cursor.execute(table_create)
    except apsw.SQLError as e:
        print(e)
        return 1
    
    return 0
        


def insert_dict(cursor, table_name, word_dict):
    """
    inserting the word_dict into the table

    arguments
    ---------

    cursor: the cursor used to communiate with the database
        type: apsw.cursor

    table_name: the name of the table
        type: string
        naming convention: school_dept_year
    
    work_dict: the dictionary containing words and frequencies
        type: dictionary
        key: string
        value: int

    return
    ------

    ...

    """

    insertion = "INSERT INTO " + table_name
    for key, value in word_dict.items():
        try:
            cursor.execute(insertion + " VALUES(?,?)" , (key, value))
        except apsw.SQLError as e:
            print(e)
            return 1
    
    return 0


def select_table(cursor, table_name):
    """
    retrieving data from a certain table

    arguments
    ---------

    cursor: the cursor used to communiate with the database
        type: apsw.cursor

    table_name: the name of the table
        type: string
        naming convention: school_dept_year
    """
    pass