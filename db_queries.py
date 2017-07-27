import os
import sqlite3
import pandas as pd

DB_PATH = os.path.dirname(__file__)+"/Tables/Pyranitar.db"

def query_level(group, experience):
    cnx = sqlite3.connect(DB_PATH)
    sql = "" \
    "SELECT level " \
    "FROM Experience " \
    "WHERE exp_group = {} " \
    "AND total_exp <= {} " \
    "ORDER BY total_exp DESC LIMIT 1".format("'"+ group + "'", experience)
    df = pd.read_sql_query(sql, cnx)
    cnx.close()
    df = df.values.flatten()
    return df[0]


def query_nature(nature):
    cnx = sqlite3.connect(DB_PATH)
    sql = "SELECT hp, atk, def, spa, spd, spe FROM Natures WHERE nature={};".format(
        "'"+ nature + "'")
    df = pd.read_sql_query(sql, cnx)
    cnx.close()
    df = list(df.values.flatten())
    return df

if __name__ == '__main__':
    print(query_nature('adamant'))
    print(query_level('slow', 50000))
