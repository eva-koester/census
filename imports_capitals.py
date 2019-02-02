# select imports of capitals only
import sqlite3
conn = sqlite3.connect('census_2.db')
cursor = conn.cursor()

cursor.execute('SELECT name, imports FROM cities INNER JOIN economies '
               'ON cities.country_code = economies.code WHERE name IN (SELECT capital FROM countries)')
print(cursor.fetchall())
