import unittest
from unittest.mock import patch
from fun_with_collections import basic_list

class BasicListTestCase(unittest.TestCase):
    def test_basic_list(self):
        with patch('builtins.input', side_effect=['cat','dog','seven']):
            self.assertEqual(['cat','dog','seven'], basic_list.get_list())

