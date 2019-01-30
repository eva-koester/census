# determine average life exp in 2010 and count no of countries with an expectancy above
import sqlite3
conn = sqlite3.connect('census_2.db')
cursor = conn.cursor()

# determine average life expectancy in 2010:
cursor.execute('SELECT AVG(life_expectancy) FROM population WHERE year = 2010')

# select everything from countries with a life expectancy greater than 1.15*average (64.78) in 2010:
cursor.execute('SELECT COUNT(*) FROM population WHERE life_expectancy > 1.15 * ('
               'SELECT AVG(life_expectancy) FROM population WHERE year = 2010) AND year = 2010')

print(cursor.fetchall())
