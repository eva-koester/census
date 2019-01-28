# sqlite3: create the new table 'census_2' in census_2.db and read in an existing table (population)
import sqlite3
import csv

# connect to the database 'census_2.db'
conn = sqlite3.connect('census_2.db')
cursor = conn.cursor()

# create the table population (should be run once and then commented out)
cursor.execute(
    '''CREATE TABLE population
         (pop_id INT NOT NULL,
         country_code TEXT NOT NULL,
         year INT NOT NULL,
         fertility_rate FLOAT NOT NULL,
         life_expectancy FLOAT NOT NULL,
         size INT NOT NULL);''')

csvReader = csv.reader(open('populations.csv'), delimiter=',', quotechar='"')
for row in csvReader:
        conn.execute('insert into population (pop_id, country_code, year, fertility_rate,'
                     'life_expectancy, size) values (?, ?, ?, ?, ?, ?)', row)

cursor.execute('SELECT * FROM population')
print(cursor.fetchall())