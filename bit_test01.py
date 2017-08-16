import unittest

class test_01(unittest.TestCase):
    arr = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
    exp_bit = [0, 3, 5, -1, 10, 5, 9, -3, 19, 7, 9, 3]
    bit_arr = [0] * len(arr)
    bit = BIT()
    def test_insert(self):
        for ind in range(len(arr)):
            bit.insert(ind, arr[ind])

        self.assertEqual(bit, exp_bit)

if __name__ == '__main__':
    unittest.main()
