from unittest import TestCase

from class_task import subtracting_two_numbers

class Test(TestCase):
    def test_subtract(self):
        number = [6-3]
        answer = [3]
        self.assertEqual(subtract_two_numbers.subtract(number), answer)
