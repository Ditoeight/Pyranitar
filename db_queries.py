import os
import sqlite3
import pandas as pd

DB_PATH = os.path.dirname(__file__)+"/Tables/Pyranitar.db"

def query_get_only_base(index, form=None):
    """
    Queries only the base stats for the Pokemon, for when you want to just
    use the statistics module and not the whole Pokemon module

    Parameters
    ----------
    index : integer, required
        The National Dex number of the pokemon you want to load

    form : string (default=None)
        The form of the pokemon you want to load

    Returns
    -------
    base_stats : list
        The base stats in the order of hp, atk, def, spa, spd, spe.

    Notes
    -----
    tyler_id is an ordering system I made that lists pokemon by their Dex
    number first then their alternates. For example the first 5 entries of
    a tyler_id sorted table would be Bulbasaur, Ivysaur, Venusaur, Mega
    Venusaur, Charmander.

    This way when the form is left blank, it pulls the "standard" form first
    when limiting the results of a dex number query to 1.

    """
    sql = "" \
    "SELECT base_hp, base_atk, base_def, base_spa, base_spd, base_spe " \
    "FROM Pokemon " \
    "WHERE dex_number = {} ".format(index)

    if form is not None:
        form_check(index, form)
        sql = sql + "AND form = {};".format("'" + form + "'")
        return run_query(sql)

    sql = sql + "ORDER BY tyler_id ASC LIMIT 1;"
    return run_query(sql)

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
    result = pd.read_sql_query(sql, cnx)
    cnx.close()
    result = list(result.values.flatten())

    return result


def form_check(index, form):
    """
    Checks the other_forms field for the Pokemon to make sure the form
    entered is valid.

    Parameters
    ----------
    index : integer, required
        The national dex number of the pokemon

    form : string, required
        The form for the pokemon being checked

    Returns
    ValueError : Error
        If there are no forms for that pokemon, or the form entered is invalid

    Nothing :
        if everything checks out

    """
    check_list_sql = "" \
    "SELECT other_forms FROM Pokemon WHERE dex_number = {}".format(index)
    check_list = run_query(check_list_sql)[0]

    if check_list is None: # If there are no forms, fuck 'em up
        raise ValueError("This Pokemon has no alternate forms.")

    check_list = check_list.split(',')
    if form not in check_list: # If it isn't there, fuck 'em up
        raise ValueError("{} is not a valid form for this Pokemon, " \
            "please use one of: {}".format(form, check_list))

if __name__ == '__main__':
    print(query_get_nature('adamant'))
    print(query_get_level('slow', 50000))
    print(query_get_experience('slow', 34))
    print(query_get_only_base(3, form='mega'))
