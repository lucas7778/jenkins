from app import Sum
import unittest

class Test(unittest.TestCase):
    def teste(self):
        self.assertEqual(Sum.sum(10,5),15)


if __name__ == '__main__':
    unittest.main()