import unittest

from python.calc import Calc


class TestCalc(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calc()

    def test_add_1(self):
        self.assertEqual(3, self.calc.add(1, 2))

    def test_add_2(self):
        self.assertEqual(0, self.calc.add(0, 0))

    def test_add_3(self):
        self.assertEqual(0.03, self.calc.add(0.01, 0.02))

    def test_add_4(self):
        self.assertEqual(-3, self.calc.add(-1, -2))

    def test_add_5(self):
        self.assertEqual("111222", self.calc.add("111", "222"))
