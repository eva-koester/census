# sqlite3: create the new table 'economies' in census_2.db and read in an existing csv file (economies)
import sqlite3
import csv

# connect to the database 'census_2.db'
conn = sqlite3.connect('census_2.db')
cursor = conn.cursor()

# create the table census_2 (should be run once and then commented out)
#cursor.execute(
#    '''CREATE TABLE economies
#         (econ_id TEXT NOT NULL,
#         code INT NOT NULL,
#         year INT NOT NULL,
#         income_group INT NOT NULL,
#         gdp_percapita INT NOT NULL,
#         gross_savings INT NOT NULL,
#         inflation_rate FLOAT NOT NULL,
#         total_investment INT NOT NULL,
#         unemployment_rate INT NOT NULL,
#         exports FLOAT NOT NULL,
#         imports INT NOT NULL);''')

csvReader = csv.reader(open('economies.csv'), delimiter=',', quotechar='"')
for row in csvReader:
        conn.execute('insert into economies (econ_id, code, year, income_group, gdp_percapita, gross_savings,'
                     'inflation_rate, total_investment, unemployment_rate, exports, imports)'
                     ' values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', row)

# store the table
conn.commit()

cursor.execute('SELECT * FROM economies')
print(cursor.fetchall())