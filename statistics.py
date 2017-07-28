#!/usr/bin/python3

"""Statistics module
"""
from db_queries import query_stats_module, query_get_nature
from experience import Experience


class Statistics(Experience):

    def __init__(self, dex_no, form=None, nature='serious', stats=None,
                 evs=[0, 0, 0, 0, 0, 0], ivs=[0, 0, 0, 0, 0, 0], current_exp=None,
                 level=100):

        pull = query_stats_module(dex_no, form)
        self.dex_no = dex_no
        self.base = pull[:6]
        exp_group = pull[6]
        self.form = pull[7]
        self.name = pull[8]

        super().__init__(exp_group=exp_group, current_exp=current_exp, level=level)

        self.evs = evs
        self.ivs = ivs
        self.nature = query_get_nature(nature)
        if stats is None:
            self.get_stats()
        else:
            self.stats = stats

    def get_stats(self, base=None, evs=None, ivs=None, nature=None):
        stats = [0, 0, 0, 0, 0, 0]

        if base is None:
            base = self.base
        if evs is None:
            evs = self.evs
        if ivs is None:
            ivs = self.ivs
        if nature is None:
            nature = self.nature

        for stat in range(6):
            if stat == 0:
                stats[stat] = int((((2 * base[stat] + ivs[stat] + (evs[stat]//4)) * \
                    self.current_level) / 100)+ self.current_level + 10)
            else:
                stats[stat] = int((((((2 * base[stat] + ivs[stat] + (evs[stat]//4))* \
                    self.current_level) / 100) + 5) * nature[stat]))
        self.stats = stats
        return self

    def set_evs(self, evs):
        self.evs = evs
        self.get_stats()
        return self

    def set_ivs(self, ivs):
        self.ivs = ivs
        self.get_stats()
        return self

    def set_nature(self, nature):
        self.nature = query_get_nature(nature)
        self.get_stats()
        return self

    def change_form(self, new_form):
        self.pull_data(self.dex_no, new_form)
        self.get_stats()
        return self

    def change_pokemon(self, dex_no, form=None):
        self.pull_data(dex_no, form)
        self.get_stats()
        super().__init__(exp_group=self.exp_group, current_exp=int(self.current_exp),
                         level=self.current_level)
        return self

    def pull_data(self, dex_no, form):
        pull = query_stats_module(dex_no, form)
        self.dex_no = dex_no
        self.base = pull[:6]
        self.exp_group = pull[6]
        self.form = pull[7]
        self.name = pull[8]
        return self

# def value_check(nature='serious', stats=None, base=(0, 0, 0, 0, 0, 0),
#                 evs=(0, 0, 0, 0, 0, 0), ivs=(0, 0, 0, 0, 0, 0)):
#     if nature not in NATURES:
#         raise ValueError("nature must be one of {}, {} was given".format(
#             NATURES.keys(), nature))


if __name__ == '__main__':
    a = Statistics(dex_no=3, nature='adamant', evs=[4, 0, 0, 252, 0, 252],
                   ivs=[31, 31, 31, 31, 31, 31])
    print(a.current_level)
    print(a.stats)
    a.set_nature('modest')
    print(a.stats)
    a.change_form('mega')
    print(a.stats)
    a.change_pokemon(25)
    print(a.stats)
