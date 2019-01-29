# sqlite3: create the new table 'census_2' in census_2.db and read in an existing table (census)
import sqlite3
import csv

# connect to the database 'census_2.db'
conn = sqlite3.connect('census_2.db')
cursor = conn.cursor()

# create the table census_2 (should be run once and then commented out)
cursor.execute(
    '''CREATE TABLE census_2
         (state INT NOT NULL,
         sex TEXT NOT NULL,
         age INT NOT NULL,
         pop2000 INT NOT NULL,
         pop2008 INT NOT NULL);''')

csvReader = csv.reader(open('census.csv'), delimiter=',', quotechar='"')
for row in csvReader:
        conn.execute('insert into census_2 (state, sex, age, pop2000, pop2008) values (?, ?, ?, ?, ?)', row)

# store the table
conn.commit()

cursor.execute('SELECT * FROM census_2')
print(cursor.fetchall())
