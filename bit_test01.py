import unittest
from bit import BIT

class test_01(unittest.TestCase):
    arr = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
    exp_bit = [0, 3, 5, -1, 10, 5, 9, -3, 19, 7, 9, 3]
    bit_arr = [0] * len(arr)
    bit = BIT(arr)

    def test_insert(self):
        self.assertEqual(self.bit._arr, self.exp_bit)


if __name__ == '__main__':
    unittest.main()
