import sqlite3
import csv
import os
import pandas as pd

path = os.path.dirname(__file__)+"/"

filename = path + 'Natures.csv'

conn = sqlite3.connect(path + 'serpyrior.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS natures(nature, hp, atk, def, spa, spd, spe)")
filename.encode('utf-8')
with open(filename) as f:
    reader = csv.reader(f)
    for field in reader:
        cur.execute("INSERT INTO natures VALUES (?,?,?,?,?,?,?);", field)

conn.commit()

df = pd.read_sql_query("SELECT * FROM natures", conn, index_col='nature')

print(df.head(25))
conn.close()
