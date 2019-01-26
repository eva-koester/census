from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, insert, select, func, \
    case, cast, Float, desc

# Define an engine to connect to the database census.db
engine = create_engine('sqlite:///census.db')
connection = engine.connect()
metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

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

