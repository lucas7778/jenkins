import unittest
from app import MMQ


class Test(unittest.TestCase):

    def test(self):
        a = MMQ([1, 2, 3], [10, 20, 30])
        b = a.mmq()
        self.assertEqual()


if __name__ == "__main__":
    unittest.main()
