import sqlite3
import os
import pandas as pd

TABLES = [['Natures', 'nature'],
          ['Experience'],
         ]

PATH = os.path.dirname(__file__)+"/"


try: # Little Bobby Tables
    os.remove(PATH + 'serpyrior.db')
except FileNotFoundError:
    pass

CONNECTION = sqlite3.connect(PATH + 'serpyrior.db')

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
