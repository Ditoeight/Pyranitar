"""Pokemon Experience Tables
"""

class ExperienceTables:
    'The table is a dictionary of the groups with a dictionary of levels'

    def __init__(self):
        #Level 1 included by default.
        self.exp_tables = {'erratic'     : {0 : 1},
                           'fast'        : {0 : 1},
                           'medium_fast' : {0 : 1},
                           'medium_slow' : {0 : 1},
                           'slow'        : {0 : 1},
                           'fluctuating' : {0 : 1},
                          }

        self.build_tables()

    def build_tables(self):
        'Fills out the exp_tables dictionary with all groups and levels'

        #erratic
        for level in range(2, 102):
            if level <= 50:
                self.exp_tables['erratic'][int(\
                    (1/50) * ((level ** 3) * (100 - level)))] = level
            elif level <= 68:
                self.exp_tables['erratic'][int(\
                    (1/100) * ((level ** 3) * (150 - level)))] = level
            elif level <= 98:
                self.exp_tables['erratic'][int(\
                    (1/500) * ((level ** 3) * ((1911 - 10 * level) / 3)))] = level
            else:
                self.exp_tables['erratic'][int(\
                    (1/100) * ((level ** 3) * (160 - level)))] = level

        #fast
        for level in range(2, 102):
            self.exp_tables['fast'][int((4 * level ** 3) / 5)] = level

        #medium_fast
        for level in range(2, 102):
            self.exp_tables['medium_fast'][int(level ** 3)] = level

        #medium_slow
        for level in range(2, 102):
            self.exp_tables['medium_slow'][int(\
                ((6 / 5) * level ** 3) - (15 * level ** 2) + (100 * level) - 140)] = level

        #slow
        for level in range(2, 102):
            self.exp_tables['slow'][int((5 * level ** 3) / 4)] = level

        #fluctuating
        for level in range(2, 102):
            if level <= 15:
                self.exp_tables['fluctuating'][int(level ** 3 * \
                    ((((level + 1) / 3) + 24) / 50))] = level
            elif level <= 36:
                self.exp_tables['fluctuating'][int(level ** 3 * \
                    ((level + 14) / 50))] = level
            else:
                self.exp_tables['fluctuating'][int(level ** 3 * \
                    (((level / 2) + 32) / 50))] = level

    def level_lookup(self, group, experience):
        'Takes in a group and experience, returns a level'
        estimate = 1
        for key in self.exp_tables[group]:
            if key <= experience:
                estimate += 1
            else:
                return estimate - 1

if __name__ == '__main__':
    a = ExperienceTables()
    print('all results should be 42')
    print(a.exp_tables['erratic'][85942], a.exp_tables['fast'][59270],
          a.exp_tables['medium_fast'][74088], a.exp_tables['medium_slow'][66505],
          a.exp_tables['slow'][92610], a.exp_tables['fluctuating'][78533])
    print(a.level_lookup('slow', 95000))
