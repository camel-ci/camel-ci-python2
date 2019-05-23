import unittest
import time

from camel_time.currenttime import getTime

class TestTime(unittest.TestCase):

    def test_time(self):
        self.assertEqual(getTime(), time.gmtime())
        self.assertNotEqual(getTime(), time.gmtime(500))

if __name__ == '__main__':
    unittest.main()
