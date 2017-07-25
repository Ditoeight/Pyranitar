from experience_tables import build_tables

EXP_TABLES = build_tables()
GROUPS = ['fluctuating', 'slow', 'medium_slow',
          'medium_fast', 'fast', 'erratic']

class Experience():
    """Experience.

    The implementation is based around experience tables created in the
    experience tables module. The Experience class will be inherited by
    the Statistics class which will ultimately be inherited by the Pokemon
    class.

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

        if group.lower() not in GROUPS:
            raise ValueError("group should be one of {}, {} was given".format(
                GROUPS, group))

        if current_exp < 0 or isinstance(current_exp, int) is False:
            raise ValueError("current_exp must be a positive whole number,"
                             " {} was given".format(current_exp))

        self.exp_group = group.lower()
        self.current_exp = current_exp
        self.get_current_level() # Calculates and sets current_level

    def get_current_level(self):
        """
        Loops through the keys of the corresponding experience table and
        increases the estimated level by 1 until it overshoots, then sets
        self.current_level to the previous estimate.

        Parameters
        ----------
        None

        Returns
        -------
        self : object
            Returns self.

        Notes
        -----
        The experience table currently goes to level 101 despite there not
        actually being a level 101. It does this so the function has a level
        to overshoot too if the pokemon is at level 100. This should probably
        be a little cleaner.

        """
        estimate = 1
        for key in EXP_TABLES[self.exp_group]:
            if key <= self.current_exp:
                estimate += 1
            else:
                self.current_level = estimate - 1
        return self

    def to_next_level(self):
        """
        Loops through the keys in the corresponding experience table. When a
        key is found that is higher than the current experience, returns the
        difference between those values.

        Parameters
        ----------
        None

        Returns
        -------
        experience : integer
            Returns the experience required to reach the next level.

        """
        for key in EXP_TABLES[self.exp_group]:
            if key > self.current_exp:
                return key - self.current_exp

    def exp_needed_to_reach(self, desired_level):
        """
        Loops through the corresponding experience table for the desired level
        and returns the difference between current_exp and experience required
        for that level.

        Parameters
        ----------
        desired_level : integer
            The level you want to know your distance to

        Returns
        -------
        experience : integer
            Returns the amount of experience needed to reach the desired_level

        """
        for key, value in EXP_TABLES[self.exp_group].items():
            if value == desired_level:
                return key - self.current_exp
    #
    # def set_experience_group(self, new_group):

    #
    # def current_experience(self, new_value):
    #     # Change the current experience to this value
    #
    # def experience_multipliers(self, **kwargs):
    #     # Change multiplier values
    #
    # def defeat_opponent(self, **kwargs):
    #     # Return experience gained from defeating opponent pokemon
    #
    # def gain_experience(self, new_current_exp):
    #     # Set current exp to new value

if __name__ == '__main__':
    a = Experience(group = 'SLOW', current_exp = 50000)
    print(a.current_level)
    print(a.exp_needed_to_reach(100))
