#!/usr/bin/python3
"""
Unittests for Square class
"""

import io
import unittest
import sys
from models.base import Base
from models.square import Square


class Test_Square(unittest.TestCase):
    """ validate test for Square """

    def test_Square1(self):
        """
        Validate the number of id
        """
        S1 = Square(5)
        self.assertEqual(S1.id, 11)
        S2 = Square(5, 2, 1, 48)
        self.assertEqual(S2.id, 48)

    def test_Square2(self):
        """
        Validate id with other types
        """
        S3 = Square(10, 2, 0, "hi")
        self.assertEqual(S3.id, "hi")
        S4 = Square(10, 2, 0, [12, 10])
        self.assertEqual(S4.id, [12, 10])
        S5 = Square(10, 2, 0, {"key": 12, "value": 20})
        self.assertEqual(S5.id, {'key': 12, 'value': 20})
        S6 = Square(10, 2, 0, (12, 10))
        self.assertEqual(S6.id, (12, 10))

    def test_Square3(self):
        """
        test Square without arguments
        """
        with self.assertRaises(TypeError):
            S7 = Square()

    def test_Square4(self):
        """
        test differents parameters
        """
        S8 = Square(24)
        self.assertEqual(S8.size, 24)
        self.assertEqual(S8.x, 0)
        self.assertEqual(S8.y, 0)

    def test_Square5(self):
        """
        test differents parameters1
        """
        S9 = Square(4, 2, 3)
        self.assertEqual(S9.size, 4)
        self.assertEqual(S9.x, 2)
        self.assertEqual(S9.y, 3)

    def test_Square6(self):
        """
        the numbers of arguments is five
        """
        with self.assertRaises(TypeError):
            S10 = Square(10, 5, 3, 1, 3)

    def test_Square7(self):
        """
        validate the type of arguments size
        """
        with self.assertRaises(TypeError):
            S11 = Square("Holberton")
        with self.assertRaises(TypeError):
            S13 = Square((4, 8))
        with self.assertRaises(TypeError):
            S14 = Square([2, 5])
        with self.assertRaises(TypeError):
            S15 = Square({"KEY": 10})

    def test_Square8(self):
        """
        validate the type of arguments x and y
        """
        with self.assertRaises(TypeError):
            S16 = Square(4, 8, "Holbie")
        with self.assertRaises(TypeError):
            S17 = Square(4, 8, [10, 4])
        with self.assertRaises(TypeError):
            S18 = Square(4, 8, (12, 20))
        with self.assertRaises(TypeError):
            S19 = Square(4, {10: 2}, 8)

    def test_Square9(self):
        """
        Validate the size of width
        """
        with self.assertRaises(ValueError):
            Square(-2)

    def test_Square10(self):
        """
        validate the position of x and y
        """
        with self.assertRaises(ValueError):
            Square(5, -1, 3)
        with self.assertRaises(ValueError):
            Square(5, 1, -3)

    def test_Square11(self):
        """
        Test the area of Square
        """
        S20 = Square(2)
        self.assertEqual(S20.area(), 4)
        S21 = Square(4, 2, 1, 6)
        self.assertEqual(S21.area(), 16)

    def test_Square12(self):
        """
        Test str of Square
        """
        S22 = Square(6, 3, 1, 8)
        self.assertEqual(S22.__str__(), "[Square] (8) 3/1 - 6")

    def test_Square13(self):
        """
        Test update of Square TEST: ID
        """
        S23 = Square(4, 8, 1, 10)
        self.assertEqual(S23.__str__(), "[Square] (10) 8/1 - 4")
        S23.update(24)
        self.assertEqual(S23.__str__(), "[Square] (24) 8/1 - 4")

    def test_Square14(self):
        """
        Test update of Square TEST:SIZE
        """
        S24 = Square(4, 8, 1, 10)
        self.assertEqual(S24.__str__(), "[Square] (10) 8/1 - 4")
        S24.update(24, 5)
        self.assertEqual(S24.__str__(), "[Square] (24) 8/1 - 5")

    def test_Square15(self):
        """
        Test update of Square TEST:X
        """
        S25 = Square(4, 8, 1, 10)
        self.assertEqual(S25.__str__(), "[Square] (10) 8/1 - 4")
        S25.update(24, 5, 7)
        self.assertEqual(S25.__str__(), "[Square] (24) 7/1 - 5")

    def test_Square16(self):
        """
        Test update of Square TEST:Y
        """
        S26 = Square(4, 8, 1, 10)
        self.assertEqual(S26.__str__(), "[Square] (10) 8/1 - 4")
        S26.update(24, 5, 7, 0)
        self.assertEqual(S26.__str__(), "[Square] (24) 7/0 - 5")

    def test_Square17(self):
        """
        Test update with invalid value
        """
        S27 = Square(8, 4, 3, 2)
        self.assertEqual(S27.__str__(), "[Square] (2) 4/3 - 8")
        with self.assertRaises(ValueError):
            S27.update(24, -5)

    def test_Square18(self):
        """
        Test update with type str in id
        """
        S28 = Square(8, 4, 3, 2)
        self.assertEqual(S28.__str__(), "[Square] (2) 4/3 - 8")
        S28.update("Holberton", 3)
        self.assertEqual(S28.__str__(), "[Square] (Holberton) 4/3 - 3")

    def test_Square19(self):
        """
        Test update with type str in id
        """
        S29 = Square(8, 4, 3, 2)
        self.assertEqual(S29.__str__(), "[Square] (2) 4/3 - 8")
        with self.assertRaises(TypeError):
            S29.update(10, "holberton")

    def test_Square20(self):
        """
        test display rectangle
        """
        S30 = Square(2)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        S30.display()
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(output, '##\n##\n')

    def test_Square21(self):
        """
        test display #1
        """
        S31 = Square(2, 3, 2)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        S31.display()
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(output, '\n' * 2 + (' ' * 3 + '#' * 2 + '\n') * 2)

    def test_Square22(self):
        """
        Test update of rectangle with **kwargs
        """
        S32 = Square(4, 8, 1, 10)
        self.assertEqual(S32.__str__(), "[Square] (10) 8/1 - 4")
        S32.update(size=1)
        self.assertEqual(S32.__str__(), "[Square] (10) 8/1 - 1")
        S32.update(size=2, x=2)
        self.assertEqual(S32.__str__(), "[Square] (10) 2/1 - 2")
        S32.update(y=1, size=2, x=3, id=89)
        self.assertEqual(S32.__str__(), "[Square] (89) 3/1 - 2")
        S32.update(x=1, size=2, y=2)
        self.assertEqual(S32.__str__(), "[Square] (89) 1/2 - 2")

    def test_Square23(self):
        """
        Test Rectangle Return a Dictionary
        """
        S33 = Square(10, 2, 1, 11)
        self.assertEqual(S33.__str__(), "[Square] (11) 2/1 - 10")
        S33_dictionary = S33.to_dictionary()
        dicts = {'id': 11, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(S33.to_dictionary(), dicts)

if __name__ == "__main__":
    unittest.main()
