import unittest
from unittest.mock import patch
from fun_with_collections import search_sort_list

class BasicListTestCase(unittest.TestCase):
    def test_get_list_below_range(self):
        with patch('builtins.input', side_effect=[-1, 10, 45]):
            with self.assertRaises(ValueError):
                search_sort_list.get_list()
    def test_get_list_above_range(self):
        with patch('builtins.input', side_effect=[1, 10, 55]):
            with self.assertRaises(ValueError):
                search_sort_list.get_list()

