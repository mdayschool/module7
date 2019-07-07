import unittest
from unittest.mock import patch
from fun_with_collections import search_sort_list
from fun_with_collections import search_sort_array
import array

class BasicListTestCase(unittest.TestCase):
    def test_get_list_below_range(self):
        with patch('builtins.input', side_effect=[-1, 10, 45]):
            with self.assertRaises(ValueError):
                search_sort_list.get_list()
    def test_get_list_above_range(self):
        with patch('builtins.input', side_effect=[1, 10, 55]):
            with self.assertRaises(ValueError):
                search_sort_list.get_list()

class SearchListTestCase(unittest.TestCase):
    def test_search_list_present(self):
        with patch('builtins.input', side_effect=[12, 25, 42]):
            self.assertEqual(1, search_sort_list.search_list(25))
    def test_search_list_absent(self):
        with patch('builtins.input', side_effect=[12, 25, 42]):
            self.assertEqual(-1, search_sort_list.search_list(34))

class SortListTestCase(unittest.TestCase):
    def test_sort_list(self):
        with patch('builtins.input', side_effect=[42, 25, 12]):
            self.assertEqual([12, 25, 42], search_sort_list.sort_list())

class SortArrayTestCase(unittest.TestCase):
    def test_sort_array(self):
        test_array = array.array('f', [12, 25, 42])
        with patch('builtins.input', side_effect=[42, 25, 12]):
            self.assertEqual(test_array, search_sort_array.sort_array())

