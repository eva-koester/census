# identify top 9 countries in terms of city count
import sqlite3
conn = sqlite3.connect('census_2.db')
cursor = conn.cursor()

cursor.execute('SELECT country_name AS country, ('
               'SELECT COUNT(*) FROM cities WHERE countries.code = cities.country_code) AS cities_num '
               'FROM cities INNER JOIN countries ON countries.code = cities.country_code GROUP BY country '
               'ORDER BY cities_num DESC, country '
               'LIMIT 9')

print(cursor.fetchall())
