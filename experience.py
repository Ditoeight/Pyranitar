#!/usr/bin/python3

from db_queries import query_get_experience, query_get_level

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

    current_exp : integer, optional (default=None)
            The current experience of the pokemon. If left blank,

    """

    def __init__(self, exp_group='slow', current_exp=None, level=100):

        value_check(group=exp_group, experience=current_exp, level=level)
        self.exp_group = exp_group.lower()
        if current_exp is None:
            self.current_level = level
            self.current_exp = query_get_experience(self.exp_group, self.current_level)
        else:
            self.current_exp = current_exp
            self.current_level = query_get_level(self.exp_group, self.current_exp)

    def exp_needed_to_level(self, to_level=None):
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

        if to_level is None: # If left blank, just set to the next level
            if self.current_level < 100:
                to_level = self.current_level + 1
            else: # If they're level 100, return 0
                return 0
        elif to_level < self.current_level:
            return 0

        value_check(level=to_level)

        return query_get_experience(self.exp_group, to_level) - self.current_exp

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
        self.current_exp = query_get_experience(self.exp_group, self.current_level)
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
        self.current_level = query_get_level(self.exp_group, self.current_exp)
        return self

def value_check(group='slow', experience=0, level=100):
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

    if level < 1 or level > 100:
        raise ValueError("level must be between 1 and 100, {} was given".format(
            level))


if __name__ == '__main__':
    a = Experience(exp_group='SLOW', current_exp = 50000)
    print(a.current_level)
    print(a.exp_needed_to_level(to_level=100))
    a.set_experience_group('fast')
    print(a.current_exp)
    a.set_current_experience(10000)
    print(a.current_level)
    print(a.exp_needed_to_level())
    a.set_current_experience(a.current_exp + 1060)
    print(a.current_level)
