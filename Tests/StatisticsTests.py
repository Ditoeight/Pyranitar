import unittest

from statistics import Statistics

class TestStatisticsMethosd(unittest.TestCase):

    def test_statisticsinitempty(self):
        stats = Statistics()
        stats.get_stats()
        current_evs = stats.get_evs()
        current_ivs = stats.get_ivs()
        current_nature = stats.get_nature()
        self.assertEqual(current_evs, (0, 0, 0, 0, 0, 0))
        self.assertEqual(current_ivs, (0, 0, 0, 0, 0, 0))
        self.assertEqual(current_nature, 'serious')
