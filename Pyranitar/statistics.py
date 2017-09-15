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

        self.__pull_data(dex_no, form)

        super().__init__(exp_group=self.exp_group, current_exp=current_exp, level=level)

        self.evs = evs
        self.ivs = ivs
        self.nature = query_get_nature(nature)
        self.get_stats()

    def get_stats(self):
        """
        Sets self.stats based on base, ivs, evs, and nature.

        Parameters
        ----------
        Nothing.

        Returns
        -------
        self : object
            Returns self.

        """
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

    def get_evs(self):
        """
        Gets EVs in a list

        Parameters
        ----------
        None.

        Returns
        ---------
        current_evs : List[integer]
            returns the list of EVs currently set for the Pokemon
        """
        return self.evs

    def set_evs(self, evs):
        """
        Sets evs to the new list

        Parameters
        ----------
        evs : list, required
            The list of evs you want to set.

        Returns
        -------
        self : object
            Returns self.

        """
        self.evs = evs
        self.get_stats()
        return self

    def get_ivs(self):
        """
        Gets IVs in a list

        Parameters
        ----------
        None.

        Returns
        ---------
        current_ivs : List[integer]
            returns the list of IVs currently set for the Pokemon
        """
        return self.ivs

    def set_ivs(self, ivs):
        """
        Sets ivs to the new list

        Parameters
        ----------
        ivs : list, required
            The list of ivs you want to set.

        Returns
        -------
        self : object
            Returns self.

        """
        self.ivs = ivs
        self.get_stats()
        return self

    def get_nature(self, nature):
        """
        Sets nature to the new nature list

        Parameters
        ----------
        None

        Returns
        -------
        self.nature : string

        """
        return self.nature


    def set_nature(self, nature):
        """
        Sets nature to the new nature list

        Parameters
        ----------
        nature : list, required
            The nature you want to set.

        Returns
        -------
        self : object
            Returns self.

        """
        self.nature = query_get_nature(nature)
        self.get_stats()
        return self

    def change_form(self, new_form):
        """
        Sets form to the new form and recalculates stats

        Parameters
        ----------
        new_form : string, required
            The new form.

        Returns
        -------
        self : object
            Returns self.

        """
        self.__pull_data(self.dex_no, new_form)
        self.get_stats()
        return self

    def change_pokemon(self, dex_no, form=None):
        """
        Changes the pokemon this instance of the object refers to.

        Parameters
        ----------
        dex_no : integer, required
            The national dex number for the pokemon you are calculating stats for.

        form : string, optional (default=None)
            The form you want to calculate for.

        Returns
        -------
        self : object
            Returns self.

        """
        self.__pull_data(dex_no, form)
        self.get_stats()
        super().__init__(exp_group=self.exp_group, current_exp=int(self.current_exp),
                         level=self.current_level)
        return self

    def __pull_data(self, dex_no, form):
        """
        Private Method

        Pulls data from the database and cuts it up into the relevant pieces.

        Parameters
        ----------
        dex_no : integer, required
            The national dex number for the pokemon you are calculating stats for.

        form : string, optional (default=None)
            The form you want to calculate for.

        Returns
        -------
        self : object
            Returns self.

        """
        pull = query_stats_module(dex_no, form)
        self.dex_no = dex_no
        self.base = pull[:6]
        self.exp_group = pull[6]
        self.form = pull[7]
        self.name = pull[8]
        return self


if __name__ == '__main__':
    a = Statistics(dex_no=3, nature='timid', evs=[252, 0, 0, 252, 0, 252],
                   ivs=[31, 31, 31, 31, 31, 31])
    print(a.current_level)
    print(a.stats)
    a.set_nature('modest')
    print(a.stats)
    a.change_form('mega')
    print(a.stats)
    a.change_pokemon(25)
    print(a.stats)
    print(a.name)
