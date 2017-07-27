import os
import sqlite3
import pandas as pd

DB_PATH = os.path.dirname(__file__)+"/Tables/Pyranitar.db"

def query_get_experience(group, level):

    sql = "" \
    "SELECT total_exp " \
    "FROM Experience " \
    "WHERE exp_group = {} " \
    "AND level = {} ".format("'"+ group + "'", level)

    return run_query(sql)[0]


def query_get_level(group, experience):

    sql = "" \
    "SELECT level " \
    "FROM Experience " \
    "WHERE exp_group = {} " \
    "AND total_exp <= {} " \
    "ORDER BY total_exp DESC LIMIT 1;".format("'"+ group + "'", experience)

    return run_query(sql)[0]


def query_get_nature(nature):

    sql = "" \
    "SELECT hp, atk, def, spa, spd, spe " \
    "FROM Natures " \
    "WHERE nature={};".format("'"+ nature + "'")

    return run_query(sql)


def run_query(sql):
    cnx = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(sql, cnx)
    cnx.close()
    df = list(df.values.flatten())
    return df

if __name__ == '__main__':
    print(query_get_nature('adamant'))
    print(query_get_level('slow', 50000))
    print(query_get_experience('slow', 34))
