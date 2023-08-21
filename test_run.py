import unittest

from run import mul


class Testmul(unittest.TestCase):

    def test_mul_function(self):
        self.assertEqual(mul(1, 2), 2)
        self.assertEqual(mul(4, 7), 28)

    def test_mul_function_with_floats(self):
        self.assertAlmostEqual(mul(2.1, 5.2), 10.92)


if __name__ == "__main__":
    unittest.main()