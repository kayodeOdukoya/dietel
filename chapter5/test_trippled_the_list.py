from unittest import TestCase

from chapter5 import trippled_the_list
class Test(TestCase):

    def test_the_list_can_tripled_multiply(self):
        number = [3, 7, 2, 6, 5]
        answer = [27, 343, 8, 216, 125]
        self.assertEqual(trippled_the_list.cube(number), answer)