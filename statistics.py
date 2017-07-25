#!/usr/bin/python3

"""Statistics module
"""
from experience import Experience

NATURES = {'serious' : (0, 0)}

class Statistics(Experience):

    def __init__(self, nature='serious', stats=None, base=(0, 0, 0, 0, 0, 0),
                 evs=(0, 0, 0, 0, 0, 0), ivs=(0, 0, 0, 0, 0, 0), exp_group='slow',
                 current_exp=0):

        super().__init__(exp_group=exp_group, current_exp=current_exp)

        if stats is None:
            self.stats = get_stats(base, evs, ivs)
        else:
            self.stats = stats

        self.base = base
        self.evs = evs
        self.ivs = ivs

    # def get_stats(self, base, evs, ivs):
    #     # Set self.stats to a list of current set_stats
    #
    # def set_evs(self, evs):
    #     # Set ev list to new ev list, run set_stats at end
    #
    # def ivs(self, ivs):
    #     # Set iv list to new iv list, run set_stats at end
    #
    # def set_nature(self, nature):
    #     # Set nature to new nature, then set_stats
    #
    # def nature_effect(self, nature):
    #     # Applies nature impact to stats, to be run in set_stats

def value_check(nature='serious', stats=None, base=(0, 0, 0, 0, 0, 0),
                evs=(0, 0, 0, 0, 0, 0), ivs=(0, 0, 0, 0, 0, 0)):
    if nature not in NATURES:
        raise ValueError("nature must be one of {}, {} was given".format(
            NATURES.keys(), nature))
