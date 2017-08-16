import unittest

from experience import Experience

class TestExperienceMethods(unittest.TestCase):

    def test_experienceinitempty(self):
        exp = Experience()
        self.assertEqual(exp.exp_group, 'slow')
        self.assertEqual(exp.current_level, 100)
        # Needs to be filled in with the correct value
        #self.assertEqual(exp.current_exp, ?)

    def test_experienceinitnonempty(self):
        exp = Experience(exp_group='Fast', current_exp=100000, level=99)
        self.assertEqual(exp.exp_group, 'fast')
        self.assertEqual(exp.current_exp, 100000)
        # Needs to be filled in with the correct level
        #self.assertEqual(exp.current_level, ?)

    def test_experienceincorrect(self):
        with self.assertRaises(ValueError):
            exp = Experience(exp_group='INVALID', current_exp=100, level=1)

        with self.assertRaises(ValueError):
            exp = Experience(exp_group='slow', current_exp=-15, level=1)

        with self.assertRaises(ValueError):
            exp = Experience(exp_group='erratic', current_exp=100, level=1000)

    def test_setexperience(self):
        exp = Experience(current_exp=0)
        self.assertEqual(exp.current_exp, 0)
        self.assertEqual(exp.current_level, 1)
        # Change the exp, EXP and Level should change
        exp.set_current_experience(1000)
        self.assertEqual(exp.current_exp, 1000)
        self.assertNotEqual(exp.current_level, 1)
