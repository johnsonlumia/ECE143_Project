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
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class SQLite():

    def __init__(self, db_name='default.db'):
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
        assert isinstance(db_name, str)

        self.__connection = apsw.Connection(db_name)
        self._cursor = self.__connection.cursor()
        logger.info(f'Database "{db_name}" created.')

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
        assert isinstance(table_name, str)
        table_create = f"CREATE TABLE {table_name}(word TINYTEXT, freq INT)"
        try:
            # execute SQL using execute, will throw SQLError when
            #   (1) the table already exists, no action needed.
            #   (2) error with in the SQL execution, error message will
            #       be printed in console
            self._cursor.execute(table_create)
        except apsw.SQLError as e:
            # print('[SQLite] ', end='')
            # print(e)
            logging.error(e)
            return 1

        logger.info(f'Table "{table_name}" created.')
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
        assert isinstance(table_name, str)
        assert isinstance(word_dict, dict)
        insertion = "INSERT INTO " + table_name
        for key, value in word_dict.items():
            try:
                self._cursor.execute(insertion + " VALUES(?,?)", (key, value))
            except apsw.SQLError as e:
                # print('[SQLite] ', end='')
                # print(e)
                logger.error(e)
                return 1

        logger.info(f'Data inserted to {table_name}')
        return 0


if __name__ == "__main__":

    # testing
    aa = dict(zip(list(range(97, 123)), list(range(97, 123))))
    test_sql = SQLite()
    test_sql.create_table("goo")
    test_sql.insert_dict("goo", aa)
