from unittest import TestCase

import tuple2
class TestTuple2(TestCase):
    def test_get_method_exist(self):
        tuple2.get_method ([10, 20, 30], (5, 15, 25))
    def test_get_method(self):
        self.assertEqual(tuple2.get_method([10, 20, 30], (5, 15, 25)), ((0, 20), (1, 25)))

