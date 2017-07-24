"""Experience Module
"""
from experience_tables import ExperienceTables

class Experience():

    def __init__(self, group=None, current_exp=0):
        # Initialize

    def current_level(self):
        # Return current level from current_exp

    def to_next_level(self):
        # Return exp required for level-up

    def exp_needed_to_reach(self, desired_level):
        # Return exp needed to get to the desired level

    def set_experience_group(self, new_group):
        # Set egg group to the new egg group

    def current_experience(self, new_value):
        # Change the current experience to this value

    def experience_multipliers(self, **kwargs):
        # Change multiplier values

    def defeat_opponent(self, **kwargs):
        # Return experience gained from defeating opponent pokemon

    def gain_experience(self, new_current_exp):
        # Set current exp to new value
