from experience_tables import build_tables

EXP_TABLES = build_tables()
GROUPS = ['fluctuating', 'slow', 'medium_slow',
          'medium_fast', 'fast', 'erratic']

class Experience():
    """The Experience Class.

    The implementation is based around experience tables created in the
    experience tables module.

    Parameters
    ----------
    group : string, required
            Specifies the experience group the pokemon belongs to.
            It must be either 'fluctuating', 'slow', 'medium_slow', 'medium_fast',
            'fast', or 'erratic', or a callable.

    current_exp : integer, optional (default=0)
            The current experience of the pokemon.

    """

    def __init__(self, group, current_exp=0):

        value_check(group=group, experience=current_exp)
        self.exp_group = group.lower()
        self.current_exp = current_exp
        self.current_level = self.find_level() # Calculates and sets current_level

    def find_level(self, group=None, experience=None, lower=1, higher=100):
        """
        Find the level through binary search.

        Parameters
        ----------
        group : string (default=None)
            The group you want to find the level in. If default None is left,
            self.exp_group is used.

        experience : integer (default=None)
            Experience value you want the level for. If default None is left,
            self.current_exp is used.

        lower : integer (default=1)
            Lower bound for the binary search.

        higher : integer (default=100)
            Upper bound for the binary search.

        Returns
        -------
        self : object
            Returns self.

        """
        if experience is None:
            experience = self.current_exp
        if group is None:
            group = self.exp_group
        value_check(group=group, experience=experience)

        midpoint = lower + ((higher - lower) // 2)

        if EXP_TABLES[group][midpoint] > experience:
            return self.find_level(lower=lower, higher=midpoint)

        elif EXP_TABLES[group][midpoint] == experience:
            return midpoint

        else:
            if EXP_TABLES[group][midpoint + 1] > experience:
                return midpoint
            elif EXP_TABLES[group][midpoint + 1] == experience:
                return midpoint + 1
            else:
                return self.find_level(lower=midpoint, higher=higher)

    def exp_needed_to_level(self, to_level=None, from_exp=None, exp_group=None):
        """
        Loops through the corresponding experience table for the desired level
        and returns the difference between starting_exp and experience required
        for the desired level.

        Parameters
        ----------
        desired_level : integer
            The level you want to know your distance to

        from_exp : integer (default=None)
            Experience you are starting from. Default becomes current object exp.

        exp_group : string (default=None)
            Experience group to calculate for. Default becomes current group.

        Returns
        -------
        experience : integer
            Returns the amount of experience needed to reach the desired_level

        """
        if to_level is None:
            if self.current_level < 100:
                to_level = self.current_level + 1
            else:
                return 0
        if from_exp is None:
            from_exp = self.current_exp
        if exp_group is None:
            exp_group = self.exp_group
        value_check(group=exp_group, experience=from_exp)
        if EXP_TABLES[exp_group][to_level] > from_exp:
            return EXP_TABLES[exp_group][to_level] - from_exp
        else:
            return 0

    def set_experience_group(self, new_group):
        """
        Verifies the new group as valid then sets the new group.

        Parameters
        ----------
        new_group : string
            The new group you want to assign

        Returns
        -------
        self : object
            Returns self.

        """
        value_check(group=new_group)
        self.exp_group = new_group
        return self

    def set_current_experience(self, new_value):
        """
        Changes the object current_exp value to the new_value

        Parameters
        ----------
        new_value : integer
            The new total experience

        Returns
        self : object
            Returns self.

        """
        value_check(experience=new_value)
        self.current_exp = new_value
        self.current_level = None
        self.current_level = self.find_level()
        return self

def value_check(group='slow', experience=0):
    """
    Makes sure values related to this module are okay.

    Parameters
    ----------
    group : string (default='slow')
        The experience group to be checked. Slow as default just so it can pass
        if left blank

    experience : integer (default=0)
        The experience value to be checked

    Returns
    -------
    ValueError : Error
        Only if the value being checked is no bueno

    """
    if group.lower() not in GROUPS:
        raise ValueError("group should be one of {}, {} was given".format(
            GROUPS, group))

    if experience < 0 or isinstance(experience, int) is False:
        raise ValueError("current_exp must be a positive whole number,"
                         " {} was given".format(experience))

if __name__ == '__main__':
    a = Experience(group = 'SLOW', current_exp = 50000)
    print(a.current_level)
    print(a.exp_needed_to_level(to_level=100))
    a.set_experience_group('fast')
    a.set_current_experience(10000)
