import csv
import sqlite3

import pandas


class Connection:
    sqlite_connection = None

    def __init__(self, db_name):
        self.db_name = db_name
        try:
            self.sqlite_connection = sqlite3.connect(db_name)
            self.cursor = self.sqlite_connection.cursor()
        except sqlite3.Error as error:
            print("Error: ", error)

    def __del__(self):
        if self.sqlite_connection is not None:
            self.sqlite_connection.commit()
            self.cursor.close()

    """
        Executes a custom query 
        
        @:param query: str
    """

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
        except sqlite3.Error as error:
            print("Error: ", error)

    """
        Makes a new table from a csv and insert to it data
        
        @:param file_path: str
        @:param table_name: str
        @:param delete_columns: str array
        @:param is_csv: boolean ( if the file is csv separated="," or tsv separated=r"\t" )
        @:param index_col: boolean ( add id primary key to the table )
    """

    def csv_to_table(
        self, file_path, table_name, delete_columns=None, is_csv=True, index_col=False
    ):
        if delete_columns is None:
            delete_columns = []
        if is_csv is True:
            csv_file = pandas.read_csv(file_path, sep=",", engine="python")
        else:
            csv_file = pandas.read_csv(file_path, sep="\t", engine="python")

        if len(delete_columns) != 0:
            csv_file.drop(columns=delete_columns)

        table_values = csv_file.values
        table_col_names = csv_file.columns.values

        self.create_table(table_name, table_col_names, index_col)

        self.insert(index_col, table_values, table_name)

    """
        Inserts data in a table
    
        @:param index_col: boolean
        @:param table_name: str
        @:param table_name: numpy array
    """

    def insert(self, index_col, table_values, table_name):
        if index_col is True:
            row_id = 1

            query = "INSERT INTO " + table_name + " VALUES \n"
            for row in table_values[: len(table_values) - 1]:
                query += "(" + str(row_id) + ","
                row_id += 1
                for i in row[: len(row) - 1]:
                    query += '"' + str(i).replace('"', " ") + '"' + ","
                query += '"' + str(row[len(row) - 1]).replace('"', " ") + '"' + "), \n"

            query += "(" + str(row_id) + ","
            row = table_values[len(table_values) - 1]
            for i in row[: len(row) - 1]:
                query += '"' + str(i).replace('"', " ") + '"' + ","
            query += '"' + str(row[len(row) - 1]).replace('"', " ") + '"' + ")"
            query += ";"
        else:
            query = "INSERT INTO " + table_name + " VALUES \n"
            for row in table_values[: len(table_values) - 1]:
                query += "("
                for i in row[: len(row) - 1]:
                    query += '"' + str(i).replace('"', " ") + '"' + ","
                query += '"' + str(row[len(row) - 1]).replace('"', " ") + '"' + "), \n"

            query += "("
            row = table_values[len(table_values) - 1]
            for i in row[: len(row) - 1]:
                query += '"' + str(i).replace('"', " ") + '"' + ","
            query += '"' + str(row[len(row) - 1]).replace('"', " ") + '"' + ")"
            query += ";"

        try:
            self.cursor.execute(query)
        except sqlite3.Error as error:
            print("Error: ", error)

    """
        Export a table to a csv file 
    
        @:param table_name: str   
    """

    def create_table(self, table_name, table_col_names, index_col=False):
        table_data = "("

        if index_col is True:
            table_data += "id INTEGER PRIMARY KEY, "

        for name in table_col_names:
            table_data += str(name)
            table_data += ","
        table_data = table_data[: len(table_data) - 1]
        table_data += ") ;"

        query = "CREATE TABLE IF NOT EXISTS '%s' " + table_data

        try:
            self.cursor.execute(query % table_name)
        except sqlite3.Error as error:
            print("Error: ", error)

    def drop_table(self, table_name):
        query = "DROP TABLE IF EXISTS '%s';"
        self.cursor.execute(query % table_name)

    """
        Export a table to a csv file 
    
        @:param table_name: str
    """

    def find_column_data(self, table_name):
        query = "PRAGMA table_info('%s') ;"

        try:
            self.cursor.execute(query % table_name)
            column_info_list = self.cursor.fetchall()

            column_names = []
            for info in column_info_list:
                column_names.append(info[1] + " " + info[2])

            return column_names

        except sqlite3.Error as error:
            print("Error: ", error)

    """
        Export a table to a csv file 
    
        @:param table_name: str
        @:param export_name: str
        @:param dir_path: str
        @:param delete_columns: str array ( columns that wont be exported )
        @:param limit: int (  )
        @:param index: boolean (adds an index to the csv)
        @:param header: boolean ( add the column named to the csv )
    """

    def export_table(
        self,
        table_name,
        export_name,
        dir_path,
        delete_columns=None,
        limit=-1,
        index=False,
        header=False,
    ):
        if delete_columns is None:
            delete_columns = []
        query = "SELECT * FROM '%s'"
        if limit != -1:
            query += "LIMIT "
            query += str(limit)

        query += ";"

        try:
            column_names = self.find_column_data(table_name)

            self.cursor.execute(query % table_name)
            records = self.cursor.fetchall()

            self.export_csv(
                records,
                column_names,
                f"{dir_path}/{export_name}.csv",
                delete_columns,
                index,
                header,
            )

        except sqlite3.Error as error:
            print("Error: ", error)

    """
        Makes a csv 
    
        @:param column_names: str array
        @:param csv_name: str
        @:param delete_columns: str array
        @:param index: boolean (adds an index to the csv)
        @:param header: boolean ( add a header to the csv )
    """

    @staticmethod
    def export_csv(
        records, column_names, csv_name, delete_columns=None, index=False, header=False
    ):
        if delete_columns is None:
            delete_columns = []
        col_num = len(column_names)
        record_array = []

        for row in records:
            record = [f"{row[0]}"]
            for i in range(1, col_num):
                record.append(f"{row[i]}")
            record_array.append(record)

        csv_data = pandas.DataFrame(record_array, columns=column_names)

        if len(delete_columns) != 0:
            csv_data = csv_data.drop(columns=delete_columns)

        csv_data.to_csv(
            csv_name, header=header, index=index, quoting=csv.QUOTE_NONE, escapechar=" "
        )
