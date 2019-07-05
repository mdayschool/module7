import unittest
from unittest.mock import patch
from fun_with_collections import basic_list

class BasicListTestCase(unittest.TestCase):
    def test_get_list_below_range(self):
        with patch('builtins.input', side_effect=[-1, 10, 45]):
            with self.assertRaises(TypeError):
                basic_list.get_list()

