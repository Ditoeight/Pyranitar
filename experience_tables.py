#!/usr/bin/python3

"""Pokemon Experience Tables
"""

def build_tables():
    exp_tables = {'erratic'     : {1 : 0},
                  'fast'        : {1 : 0},
                  'medium_fast' : {1 : 0},
                  'medium_slow' : {1 : 0},
                  'slow'        : {1 : 0},
                  'fluctuating' : {1 : 0},}

    # erratic
    for level in range(2, 102):
        # Consistent Experience tables first; these hold to the same formula
        # regardless of level. No conditionals necessary
        exp_tables['fast'][level] = int((4 * level ** 3) / 5)
        exp_tables['medium_fast'][level] = int(level ** 3)
        exp_tables['medium_slow'][level] = int(\
            ((6/5) * level ** 3) - (15 * level ** 2) + (100 * level) - 140)
        exp_tables['slow'][level] = int((5 * level ** 3) / 4)

        # Conditionals necessary for erratic and fluctuating.

        if level <= 50:
            exp_tables['erratic'][level] = int(\
                (1/50) * ((level ** 3) * (100 - level)))

            if level <= 15:
                exp_tables['fluctuating'][level] = int(\
                level ** 3 * ((((level + 1) / 3) + 24) / 50))
            elif level <= 36:
                exp_tables['fluctuating'][level] = int(\
                level ** 3 * ((level + 14) / 50))
            else:
                exp_tables['fluctuating'][level] = int(\
                level ** 3 * (((level / 2) + 32) / 50))

        elif level <= 68:
            exp_tables['erratic'][level] = int(\
                (1/100) * ((level ** 3) * (150 - level)))

            exp_tables['fluctuating'][level] = int(\
                level ** 3 * (((level / 2) + 32) / 50))

        elif level <= 98:
            exp_tables['erratic'][level] = int(\
                (1/500) * ((level ** 3) * ((1911 - 10 * level) / 3)))

            exp_tables['fluctuating'][level] = int(\
                level ** 3 * (((level / 2) + 32) / 50))

        else:
            exp_tables['erratic'][level] = int(\
                (1/100) * ((level ** 3) * (160 - level)))

            exp_tables['fluctuating'][level] = int(\
                level ** 3 * (((level / 2) + 32) / 50))

        return exp_tables
