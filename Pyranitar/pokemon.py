#!/usr/bin/python3

"""Pokemon module
"""

from statistics import Statistics
from db_queries import query_experience_yield

class Pokemon(Statistics):

    def __init__(self, dex_no, form=None, nature='serious', evs=(0, 0, 0, 0, 0, 0),
                 ivs=(0, 0, 0, 0, 0, 0), current_exp=None, level=100, hold_item=None,
                 original_trainer=True, ):
        super(Pokemon, self).__init__(dex_no=dex_no, form=form, nature=nature, evs=evs,
                                      ivs=ivs, current_exp=current_exp, level=level)

    def defeat(self, enemy_dex, enemy_level, form=None):
        pass
