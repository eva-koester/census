# sqlilte: create the new database 'census_2'
import sqlite3

# create the database
conn = sqlite3.connect('census_2.db')
cursor = conn.cursor()
