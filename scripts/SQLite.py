#
# ECE 143 Group Project
#
# A class that simplifies usage of apsw package for project use
#   connects and manipulates database (SQLite)
#
# by Renjie Zhu on Nov 4, 2018
#
#

import apsw


class SQLite():

    def __init__(self, db_name='test.db'):
        """
        initializing a connection with a database

        arguments
        ---------

        db_name: the name of the database
            type: string

        return
        ------
        an SQLite object
        """
        self.__connection = apsw.Connection(db_name)
        self._cursor = self.__connection.cursor()

    def create_table(self, table_name):
        """
        create a table in SQLite with a name

        the table will be structured like following
            word: tinystr
            freq: int

        arguments
        ---------

        table_name: the name of the table
            type: string
            naming convention: school_dept_year

        return
        ------

        error code
            type: int
            0: no errors
            1: error occurs (table exist)
            .
            .

        """

        table_create = f"CREATE TABLE {table_name}(word TINYTEXT, freq INT)"
        try:
            self._cursor.execute(table_create)
        except apsw.SQLError as e:
            print(e)
            return 1

        return 0

    def insert_dict(self, table_name, word_dict):
        """
        inserting the word_dict into the table

        arguments
        ---------

        table_name: the name of the table
            type: string
            naming convention: school_dept_year

        work_dict: the dictionary containing words and frequencies
            type: dictionary
            key: string
            value: int

        return
        ------

        error code
            type: int
            0: no errors
            1: error occurs (table exist)

        ...

        """

        insertion = "INSERT INTO " + table_name
        for key, value in word_dict.items():
            try:
                self._cursor.execute(insertion + " VALUES(?,?)", (key, value))
            except apsw.SQLError as e:
                print(e)
                return 1

        return 0

    def select_entry_in_table(self, entry, table_name):
        pass


if __name__ == "__main__":
    aa = dict(zip(list(range(97, 123)), list(range(97, 123))))
    test_sql = SQLite()
    test_sql.create_table("goo")
    test_sql.insert_dict("goo", aa)
