# get the metroarea population of capital cities
import sqlite3
conn = sqlite3.connect('census_2.db')
cursor = conn.cursor()

cursor.execute('SELECT name, country_code, metroarea_pop FROM cities WHERE name IN (SELECT capital FROM countries) '
               'ORDER BY urbanarea_pop DESC')
print(cursor.fetchall())
