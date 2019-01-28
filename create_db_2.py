# sqlite3create the new database 'census_2' and read in an existing table (census)
import sqlite3
import csv

# create the database
conn = sqlite3.connect('census_2.db')
cursor = conn.cursor()

# create the table census_2
cursor.execute(
    '''CREATE TABLE census_2
         (state INT NOT NULL,
         sex TEXT NOT NULL,
         age INT NOT NULL,
         pop2000 INT NOT NULL,
         pop2008 INT NOT NULL);''')

# the sqlite command '.import' did not work, I therefore used another method to read in the csv
#sqlite> .__import__(c:/census.csv census_2)
csvReader = csv.reader(open('census.csv'), delimiter=',', quotechar='"')
for row in csvReader:
        conn.execute('insert into census_2 (state, sex, age, pop2000, pop2008) values (?, ?, ?, ?, ?)', row)

#cursor.execute('SELECT * FROM census_2')