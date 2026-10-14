import unittest
from random_guess import run_guess

class TestMain(unittest.TestCase):
    def test_input(self):
        self.assertTrue(run_guess(5, 5))

    def test_wrong(self):
        self.assertFalse(run_guess(1, 5))

    def test_limit(self):
        self.assertFalse(run_guess(11, 5))

    def test_string(self):
        self.assertFalse(run_guess(1, '5'))


if __name__ == '__main__':
    unittest.main()
