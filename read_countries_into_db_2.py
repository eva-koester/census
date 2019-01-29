# sqlite3: create the new table 'countries' in census_2.db and read in an existing csv file (countries)
import sqlite3
import csv

# connect to the database 'census_2.db'
conn = sqlite3.connect('census_2.db')
cursor = conn.cursor()

# create the table census_2 (should be run once and then commented out)
cursor.execute(
    '''CREATE TABLE countries
         (code TEXT NOT NULL,
          country_name TEXT NOT NULL,
          continent TEXT NOT NULL,
          region TEXT NOT NULL,
          surface_area INT NOT NULL,
          indep_year INT NOT NULL,
          local_name TEXT NOT NULL,
          gov_form TEXT NOT NULL,
          capital TEXT NOT NULL,
          cap_long FLOAT NOT NULL,
          cap_lat FLOAT NOT NULL);''')

csvReader = csv.reader(open('countries.csv'), delimiter=',', quotechar='"')
for row in csvReader:
        conn.execute('insert into countries (code, country_name, continent, region, surface_area, indep_year,'
                     'local_name, gov_form, capital, cap_long, cap_lat) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', row)

# store the table
conn.commit()

cursor.execute('SELECT * FROM countries')
print(cursor.fetchall())