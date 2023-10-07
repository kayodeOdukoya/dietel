from unittest import TestCase

import list_exercise

class TestListExercise(TestCase):
    def test_add_function_exist(self):
        list_exercise.add_function([15, 20, 25, 20, 10, 5])

    def test_add_function(self):
        self.assertEqual(list_exercise.add_function([15, 20, 25, 20, 10, 5]), 95)

    def test_multiply_function(self):
        self.assertEqual(list_exercise.multiply_function([15, 20, 25, 20, 10, 5]), 7500000)

    def test_for_larget_function(self):
        self.assertEqual(list_exercise.find_largest([15, 20, 25, 20, 10, 5]), 25)

    def test_for_smallest_function(self):
        self.assertEqual(list_exercise.find_smallest([15, 20, 25, 20, 10, 5]), 5)

    def test_no_duplicate_function(self):
        self.assertEqual(list_exercise.no_duplicate([15, 20, 25, 20, 10, 5]), 15, 25, 20, 10, 5)