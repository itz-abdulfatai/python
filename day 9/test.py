import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        print("about to test a function") #runs before each unit test

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)


    def test_do_stuf2(self):
        test_param = 'z'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)
    def test_do_stuf3(self):
        '''yoooo '''
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please input a number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please input a number')

    def tearDown(self):
        print('cleaning up') # runs after every unit test


if __name__ == '__main__':
    unittest.main()
