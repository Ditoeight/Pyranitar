"""Pokemon Experience Tables
"""

def build_tables():
    exp_tables = {'erratic'     : {0 : 1},
                  'fast'        : {0 : 1},
                  'medium_fast' : {0 : 1},
                  'medium_slow' : {0 : 1},
                  'slow'        : {0 : 1},
                  'fluctuating' : {0 : 1},}

    for level in range(2, 102):
        if level <= 50:
            exp_tables['erratic'][int(\
                (1/50) * ((level ** 3) * (100 - level)))] = level
        elif level <= 68:
            exp_tables['erratic'][int(\
                (1/100) * ((level ** 3) * (150 - level)))] = level
        elif level <= 98:
            exp_tables['erratic'][int(\
                (1/500) * ((level ** 3) * ((1911 - 10 * level) / 3)))] = level
        else:
            exp_tables['erratic'][int(\
                (1/100) * ((level ** 3) * (160 - level)))] = level

    #fast
    for level in range(2, 102):
        exp_tables['fast'][int((4 * level ** 3) / 5)] = level

    #medium_fast
    for level in range(2, 102):
        exp_tables['medium_fast'][int(level ** 3)] = level

    #medium_slow
    for level in range(2, 102):
        exp_tables['medium_slow'][int(\
            ((6 / 5) * level ** 3) - (15 * level ** 2) + (100 * level) - 140)] = level

    #slow
    for level in range(2, 102):
        exp_tables['slow'][int((5 * level ** 3) / 4)] = level

    #fluctuating
    for level in range(2, 102):
        if level <= 15:
            exp_tables['fluctuating'][int(level ** 3 * \
                ((((level + 1) / 3) + 24) / 50))] = level
        elif level <= 36:
            exp_tables['fluctuating'][int(level ** 3 * \
                ((level + 14) / 50))] = level
        else:
            exp_tables['fluctuating'][int(level ** 3 * \
                (((level / 2) + 32) / 50))] = level
        return exp_tables
