from unittest import TestCase
import reverse_tuple
class TestReverseTuple(TestCase):
    def test_reverse_tuple(self):
        number = (10, 20, 30, 40, 50)
        answer = (50, 40, 30, 20, 10)
        assertEqual(tuple.reverse_tuple(number), answer)