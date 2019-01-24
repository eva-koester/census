# Project: use sqlalchemy to connect to a sqlite database and do some manipulations
# Import the necessary modules
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, insert, select, func, \
    case, cast, Float, desc
import csv

# Define an engine to connect to the database "sqlite":
engine = create_engine('sqlite:///sqlite')
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

## build a query to determine average age of population
# Calculate weighted average age, group by sex
stmt = select([census.columns.sex,
               (func.sum(census.columns.age * census.columns.pop2008) /
                func.sum(census.columns.pop2008)).label('average_age')])
stmt = stmt.group_by(census.columns.sex)

# Execute the query and store it in results
results = connection.execute(stmt).fetchall()

# Print the average age by sex
for result in results:
    print(result.sex, result.average_age)

## build a query to determine the Percentage of Population by Gender and State in 2000
stmt = select([census.columns.state,
    (func.sum(case([(census.columns.sex == 'F', census.columns.pop2000)], else_=0)) /
     cast(func.sum(census.columns.pop2000), Float) * 100).label('percent_female')])

# Group stmt by state, execute the query, store results and execute the query
stmt = stmt.group_by(census.columns.state)
results = connection.execute(stmt).fetchall()
for result in results:
    print(result.state, result.percent_female)

## Build query to return state name and population difference from 2008 to 2000
stmt = select([census.columns.state,(census.columns.pop2008 - census.columns.pop2000).label('pop_change')])

# Group by State, Order by Population Change, Limit to top 10
stmt = stmt.group_by(census.columns.state)
stmt = stmt.order_by(desc('pop_change'))
stmt = stmt.limit(10)

# Use connection to execute the statement and fetch all results, print the
# state and population change for each record
results = connection.execute(stmt).fetchall()
for result in results:
    print('{}:{}'.format(result.state, result.pop_change))

