# sqlite3: create the new table 'cities' in census_2.db and read in an existing csv file (cities)
import sqlite3
import csv

# connect to the database 'census_2.db'
conn = sqlite3.connect('census_2.db')
cursor = conn.cursor()

# create the table census_2 (should be run once and then commented out)
cursor.execute(
    '''CREATE TABLE cities
         (name TEXT NOT NULL,
         country_code INT NOT NULL,
         city_proper_pop INT NOT NULL,
         metroarea_pop INT NOT NULL,
         urbanarea_pop INT NOT NULL);''')

csvReader = csv.reader(open('cities.csv'), delimiter=',', quotechar='"')
for row in csvReader:
        conn.execute('insert into cities (name, country_code, city_proper_pop, metroarea_pop, urbanarea_pop)'
                     ' values (?, ?, ?, ?, ?)', row)

# store the table
conn.commit()

cursor.execute('SELECT * FROM cities')
print(cursor.fetchall())