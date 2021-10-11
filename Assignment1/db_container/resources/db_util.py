import os

import pandas as pd
import sqlalchemy as db
from sqlalchemy import Column, Float, Table, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class DBUtil:

    def __init__(self):
        # The database URL is provided as an env. variable
        if 'DB_URL' in os.environ:
            db_url = os.environ['DB_URL']
        else:
            db_url = 'sqlite:///features.db'
        # create the database
        self.engine = db.create_engine(db_url, echo=True)
        self._reflect()

    def create_tb(self, table_name, column_names):
        # Get a connection to the database
        conn = self.engine.connect()
        self._reflect()
        # Start the database transaction
        trans = conn.begin()
        # Define the columns of the table. Assume that a list of column names are provided and column type is float.
        string_columns = ["Access", "AirType", "Amenities", "Heat", "Latitude", "Longitude", "PropType", "Roof", "TotSqf"]
        columns = (Column(name, String, quote=False)if name in string_columns else Column(name, Float, quote=False) for name in column_names)
        # Create the table. Id is the primary key and it will be automatically generated.
        v_table = Table(table_name, self.Base.metadata, Column('id', Integer, primary_key=True, autoincrement=True),
                        extend_existing=True, *columns)
        v_table.create(self.engine, checkfirst=True)
        # End the database transaction
        trans.commit()

    def drop_tb(self, table_name):
        conn = self.engine.connect()
        trans = conn.begin()
        self._reflect()
        # get a reference to the table
        v_table = self.Base.metadata.tables[table_name]
        v_table.drop(self.engine, checkfirst=True)
        trans.commit()

    def add_data_records(self, table_name, records):
        self._reflect()
        # get a reference to the table
        v_table = self.Base.metadata.tables[table_name]
        # get a query object for inserting data
        query = db.insert(v_table)
        connection = self.engine.connect()
        trans = connection.begin()
        # run the query
        connection.execute(query, records)
        trans.commit()

    def read_data_records(self, table_name):
        self._reflect()
        v_table = self.Base.metadata.tables[table_name]
        connection = self.engine.connect()
        trans = connection.begin()
        # get a query object for reading all data
        query = db.select([v_table])
        # read all data
        df = pd.read_sql_query(query, con=connection)
        trans.commit()
        return df

    # refresh meta-data
    def _reflect(self):
        self.Base = declarative_base()
        self.Base.metadata.reflect(self.engine)
