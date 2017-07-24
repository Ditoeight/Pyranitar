"""Experience Module
"""
from experience_tables import build_tables

EXP_TABLES = build_tables()

class Experience():

    def __init__(self, group=None, current_exp=0):
        self.exp_group = group.lower()
        self.current_exp = current_exp

    def current_level(self):
        'Returns the current level based on current experience and group'
        estimate = 1
        for key in EXP_TABLES[self.exp_group]:
            if key <= self.current_exp:
                estimate += 1
            else:
                return estimate - 1

    def to_next_level(self):
        'Takes a group and experience, returns exp to next level'
        for key in EXP_TABLES[self.exp_group]:
            if key > self.current_exp:
                return key - self.current_exp
    #
    # def exp_needed_to_reach(self, desired_level):
    #     # Return exp needed to get to the desired level
    #
    # def set_experience_group(self, new_group):
    #     # Set egg group to the new egg group
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
    print(a.current_level())
    print(a.to_next_level())
