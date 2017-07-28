#!/usr/bin/python3

"""Statistics module
"""
from db_queries import query_get_only_base, query_get_nature
from experience import Experience


class Statistics(Experience):

    def __init__(self, dex_no=None, form=None, nature='serious', stats=None,
                 base=[0, 0, 0, 0, 0, 0], evs=[0, 0, 0, 0, 0, 0],
                 ivs=[0, 0, 0, 0, 0, 0], exp_group='slow', current_exp=0):

        super().__init__(exp_group=exp_group, current_exp=current_exp)

        self.evs = evs
        self.ivs = ivs
        self.base = base
        if dex_no is not None:
            self.base = query_get_only_base(dex_no, form)
        self.nature = query_get_nature(nature)
        if stats is None:
            self.stats = self.get_stats(self.base, self.evs, self.ivs, self.nature)
        else:
            self.stats = stats

    def get_stats(self, base, evs, ivs, nature):
        stats = [0, 0, 0, 0, 0, 0]

        for stat in range(len(stats)):
            print(stat)
            if stat == 0:
                stats[stat] = int((((2 * base[stat] + ivs[stat] + (evs[stat]/4)) * \
                    self.current_level) / 100)+ self.current_level + 10)
            else:
                stats[stat] = int((((((2 * base[stat] + ivs[stat] + (evs[stat]))* \
                    self.current_level) / 100) + 5) * nature[stat]))
        return stats
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

# def value_check(nature='serious', stats=None, base=(0, 0, 0, 0, 0, 0),
#                 evs=(0, 0, 0, 0, 0, 0), ivs=(0, 0, 0, 0, 0, 0)):
#     if nature not in NATURES:
#         raise ValueError("nature must be one of {}, {} was given".format(
#             NATURES.keys(), nature))


if __name__ == '__main__':
    a = Statistics(dex_no=3, nature='adamant',current_exp=50000)
    print(a.current_level)
    print(a.stats)
