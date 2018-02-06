# Maak een kleine textfile van de eerste 10 artikelen
import sqlite3

conn = sqlite3.connect('example.db')
cur = conn.cursor()

sql_line = "select body from headline_table limit 10;"

all_bodies = cur.execute(sql_line)
print(all_bodies)

conn.close()