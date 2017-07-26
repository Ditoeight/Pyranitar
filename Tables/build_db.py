import sqlite3
import os
import pandas as pd

TABLES = [['Natures', 'nature'],
          ['Experience'],
         ]

PATH = os.path.dirname(__file__)+"/"
CONNECTION = sqlite3.connect(PATH + 'serpyrior.db')

# insert a little jimmy drop tables here


for table in TABLES:
    table_name = table[0]
    print(table_name)
    try:
        table_index = table[1]
        write_index = False
    except IndexError:
        table_index = None
        write_index = True

    df = pd.read_csv(PATH + table_name + '.csv')
    df.to_sql(table_name, CONNECTION, index=write_index, index_label=table_index)

CONNECTION.commit()
CONNECTION.close()

# cur = conn.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS natures()")
# filename.encode('utf-8')
# with open(filename) as f:
#     reader = csv.reader(f)
#     for field in reader:
#         cur.execute("INSERT INTO natures VALUES (?,?,?,?,?,?,?);", field)
#
# conn.commit()
#
# df = pd.read_sql_query("SELECT * FROM natures", conn, index_col='nature')
#
# print(df.head(25))
# conn.close()
