#!/usr/bin/python3
"""
Unit tests for Base class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Base(unittest.TestCase):
    """Base class tests"""
    def test_validate(self):
        """ validate the id number, without args """
        A1 = Base()
        self.assertEqual(A1.id, 1)
        A2 = Base()
        self.assertEqual(A2.id, 2)
        A3 = Base()
        self.assertEqual(A3.id, 3)

    def test_validate1(self):
        """ validate the id number, with args """
        B1 = Base(25)
        self.assertEqual(B1.id, 25)
        B2 = Base(-13)
        self.assertEqual(B2.id, -13)

    def test_validate2(self):
        """ validate the id number, with 2 or more args"""
        with self.assertRaises(TypeError):
            C1 = Base(3, 7)

    def test_validate3(self):
        """ validate if the args is str """
        D1 = Base("13")
        self.assertEqual(D1.id, "13")

    def test_validate4(self):
        """ validate if the args is str """
        E1 = Base((1, 2))
        self.assertEqual(E1.id, (1, 2))

    def test_validate5(self):
        """ validate if the args is str """
        F1 = Base({"hi": 10, "betty": 20})
        self.assertEqual(F1.id, {"hi": 10, "betty": 20})

    def test_validate6(self):
        """ validate if the args is str"""
        G1 = Base([1, 2])
        self.assertEqual(G1.id, [1, 2])

if __name__ == "__main__":
    unittest.main()
