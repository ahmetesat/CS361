__author__ = 'aaa'

import unittest
import Main.PMI


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Main.PMI.kk(Main.PMI.a),Main.PMI.lklength(Main.PMI.a), 3)
        



if __name__ == '__main__':
    unittest.main()
