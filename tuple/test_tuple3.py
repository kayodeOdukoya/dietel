from unittest import TestCase

import tuple3
class TestTuple3(TestCase):
    def test_swap_elements_exist(self):
        tuple3.swap_elements([15, 25, 60, 50, 30, 40, 45, 55])
    def test_swap_elements(self):
        self.assertEqual(tuple3.swap_elements([15, 25, 60, 50, 30, 40, 45, 55]), (55, 15))