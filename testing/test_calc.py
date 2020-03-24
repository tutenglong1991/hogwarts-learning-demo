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

    def test_add_6(self):
        self.assertEqual([1, 2], self.calc.add([1], [2]))

    def test_add_7(self):
        self.assertEqual((1, 2, 3, 4), self.calc.add((1, 2), (3, 4)))

    def test_add_8(self):
        self.assertNotEqual((1, 2, 3, 4), self.calc.add((1, 3), (2, 4)))

    # TypeError: unsupported operand type(s) for +: 'set' and 'set'
    # def test_add_9(self):
    #     self.assertNotEqual({1, 2, 3}, self.calc.add({1, 3}, {2, 3}))

    # def test_add_10(self):
    #     self.assertEqual({"a": 1, "b": 2}, self.calc.add({"a", 1}, {"b", 2}))


if __name__ == '__main__':
    unittest.main()
