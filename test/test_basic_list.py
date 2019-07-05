import unittest
from unittest.mock import patch
from fun_with_collections import search_sort_list

class BasicListTestCase(unittest.TestCase):
    def test_basic_list(self):
        with patch('builtins.input', side_effect=['cat','dog','seven']):
            self.assertEqual(['cat','dog','seven'], search_sort_list.get_list())

