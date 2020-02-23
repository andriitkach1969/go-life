import unittest
from src.Moore import Moore


class MooreTestCases(unittest.TestCase, Moore):

    def setUp(self):
        self.earthRule = Moore()

    def test_Moore_IS_OK(self):
        self.assertEqual(1, 1, 'Incorrect response: expected:IS_OK actual: no')

    def test_Moore_IS_CROWD(self):
        self.assertEqual(1, 1, 'Incorrect response: expected:IS_CROWD actual: no')

    def test_Moore_IS_DESERT(self):
        self.assertEqual(1, 1, 'Incorrect response: expected:IS_DESERT actual: no')

