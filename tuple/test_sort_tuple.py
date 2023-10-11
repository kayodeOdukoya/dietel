from unittest import TestCase

import sort_tuple
class TestSortTuple(TestCase):
    def test_sorted_tuple_exist(self):
        sort_tuple.sorted_tuple([(('a', 23), ('b', 37), ('c', 11), ('d', 29))])
    def test_sorted_turple(self):
        self.assertEqual(sort_tuple.sorted_tuple([(('a', 23), ('b', 37), ('c', 11), ('d', 29))]), (('c', 11), ('a', 23), ('d', 29), ('b', 37)))
