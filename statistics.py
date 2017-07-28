#!/usr/bin/python3

"""Statistics module
"""
from db_queries import query_stats_module, query_get_nature
from experience import Experience


class Statistics(Experience):
    """The Statistics Class.

    Parameters
    ----------
    dex_no : integer, required
        The national dex number for the pokemon you are calculating stats for.

    form : string, optional (default=None)
        The form you want to calculate for, default is the most base form.
        In unique cases like with Meowstic and Basculin, the default form is
        just whichever one I decided to list first.

    nature : string, optional (default='serious')
        The nature you want to have an effect on the stats. Default is serious
        because that one doesn't do anything.

    evs : list, optional (default=(0, 0, 0, 0, 0, 0))
        The list of EVs in the standard order.

    ivs : list, optional (default=(0, 0, 0, 0, 0, 0))
        The list of IVs in the standard order.

    current_exp : integer, optional (default=None)
        The current exp, is used to calculate level if level is not given

    level : integer, optional (default=None)
        The level for the pokemon. If both exp and level are entered, exp
        is prioritized.

    """

    def __init__(self, dex_no, form=None, nature='serious', evs=(0, 0, 0, 0, 0, 0),
                 ivs=(0, 0, 0, 0, 0, 0), current_exp=None, level=100):

        pull = query_stats_module(dex_no, form)

        self.dex_no = dex_no
        self.base = pull[:6]
        self.exp_group = pull[6]
        self.form = pull[7]
        self.name = pull[8]

        super().__init__(exp_group=self.exp_group, current_exp=current_exp, level=level)

        self.evs = evs
        self.ivs = ivs
        self.nature = query_get_nature(nature)
        self.get_stats()

    def get_stats(self):
        stats = [0, 0, 0, 0, 0, 0]

        for stat in range(6):
            if stat == 0:
                stats[stat] = int((((2 * self.base[stat] + self.ivs[stat] + (self.evs[stat]//4)) * \
                    self.current_level) / 100)+ self.current_level + 10)
            else:
                stats[stat] = int((((((2 * self.base[stat] + self.ivs[stat] + \
                    (self.evs[stat] // 4)) * self.current_level) / 100) + 5) * self.nature[stat]))
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
