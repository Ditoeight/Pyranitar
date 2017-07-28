import os
import sqlite3
import pandas as pd

DB_PATH = os.path.dirname(__file__)+"/Tables/Pyranitar.db"

def query_get_experience(group, level):
    """
    Queries against the experience table to return total_exp for the level
    in the provided experience group.

    Parameters
    ----------
    group : string, required
        The experience group you want to query against.

    level : integer, required
        The level you want the minimum experience for.

    Returns
    -------
    experience : integer
        The total_exp required for the given level and experience group.

    """

    sql = "" \
    "SELECT total_exp " \
    "FROM Experience " \
    "WHERE exp_group = {} " \
    "AND level = {};".format("'"+ group + "'", level)

    return run_query(sql)[0]


def query_get_level(group, experience):
    """
    Queries against the experience table to return the level that would be
    reached given the experience and exp_group

    Parameters
    ----------
    group : string, required
        The experience group you want to query against.

    experience : integer, required
        The experience you want to find the level for.

    Returns
    -------
    level : integer
        The level that would be reached given the group and experience.

    """

    sql = "" \
    "SELECT level " \
    "FROM Experience " \
    "WHERE exp_group = {} " \
    "AND total_exp <= {} " \
    "ORDER BY total_exp DESC LIMIT 1;".format("'"+ group + "'", experience)

    return run_query(sql)[0]


def query_get_nature(nature):
    """
    Queries against the nature table to return a list with the stat effects
    of that nature.

    Parameters
    ----------
    nature : string, required
        The nature you want the stat effects for.

    Returns
    -------
    stat_effects : list
        A list of the stat effects in the order of hp, atk, def, spa, spd, spe.

    """

    sql = "" \
    "SELECT hp, atk, def, spa, spd, spe " \
    "FROM Natures " \
    "WHERE nature={};".format("'"+ nature + "'")

    return run_query(sql)


def run_query(sql):
    """
    Connects to the database and runs a query. Only intended for single-line
    returns from queries.

    Parameters
    ----------
    sql : string, required
        The full SQL command to be run

    Returns
    -------
    results : list
        Returns a list with the results from the query

    Notes
    -----
    This function will work if you do something like SELECT * FROM table,
    but all the results will be converted into a one-dimensional list.

    """
    
    cnx = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(sql, cnx)
    cnx.close()
    df = list(df.values.flatten())

    return df

if __name__ == '__main__':
    print(query_get_nature('adamant'))
    print(query_get_level('slow', 50000))
    print(query_get_experience('slow', 34))
