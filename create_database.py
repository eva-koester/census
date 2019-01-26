# Project: use sqlalchemy to connect to a sqlite database and do some manipulations
# Import the necessary modules
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, insert, select, func, \
    case, cast, Float, desc
import csv

# Define an engine to connect to the database census.db
engine = create_engine('sqlite:///census.db')
connection = engine.connect()

# Initialize MetaData (to keep together the features of the table) and build a census table
metadata = MetaData()
census = Table('census', metadata,
               Column('state', String(30)),
               Column('sex', String(1)),
               Column('age', Integer()),
               Column('pop2000', Integer()),
               Column('pop2008', Integer()))

# Create the table in the database
metadata.create_all(engine)

# read in the csv file:
# build the csv_reader to iterate over the csv file
csvfile = open('census.csv', newline='')
print(csvfile)
csv_reader = csv.reader(csvfile)
# Create an empty list, iterate over rows in csv_reader
values_list = []
for row in csv_reader:
    data = {'state': row[0], 'sex': row[1], 'age': row[2], 'pop2000': row[3], 'pop2008': row[4]}
    values_list.append(data)

# Build insert statement and use the values_list to insert data
stmt = insert(census)
results = connection.execute(stmt, values_list)

# make sure that rowcount equals 8772
assert results.rowcount == 8772
