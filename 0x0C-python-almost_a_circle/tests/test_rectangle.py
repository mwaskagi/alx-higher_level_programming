#!/usr/bin/python3
"""
Unittests for Rectangle class
"""


import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """ validate test for Rectangle """

    def test_Rectangle1(self):
        """
        Validate the number of id
        """
        R1 = Rectangle(10, 2)
        self.assertEqual(R1.id, 4)
        R2 = Rectangle(2, 10)
        self.assertEqual(R2.id, 5)
        R3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(R3.id, 12)

    def test_Rectangle2(self):
        """
        validate the id with other types
        """
        R4 = Rectangle(10, 2, 0, 0, "hi")
        self.assertEqual(R4.id, "hi")
        R5 = Rectangle(10, 2, 0, 0, [12, 10])
        self.assertEqual(R5.id, [12, 10])
        R6 = Rectangle(10, 2, 0, 0, {"key": 12, "value": 20})
        self.assertEqual(R6.id, {'key': 12, 'value': 20})
        R7 = Rectangle(10, 2, 0, 0, (12, 10))
        self.assertEqual(R7.id, (12, 10))

    def test_Rectangle3(self):
        """
        test rectangle without arguments
        """
        with self.assertRaises(TypeError):
            R8 = Rectangle()

    def test_Rectangle4(self):
        """
        test with one argument
        """
        with self.assertRaises(TypeError):
            R9 = Rectangle(98)

    def test_Rectangle5(self):
        """
        test differents parameters
        """
        R10 = Rectangle(24, 98)
        self.assertEqual(R10.width, 24)
        self.assertEqual(R10.height, 98)
        self.assertEqual(R10.x, 0)
        self.assertEqual(R10.y, 0)

    def test_Rectangle6(self):
        """
        test differents parameters1
        """
        R11 = Rectangle(24, 98, 2, 3)
        self.assertEqual(R11.width, 24)
        self.assertEqual(R11.height, 98)
        self.assertEqual(R11.x, 2)
        self.assertEqual(R11.y, 3)

    def test_Rectangle7(self):
        """
        the numbers of arguments is six
        """
        with self.assertRaises(TypeError):
            R12 = Rectangle(10, 5, 3, 1, 3, 34)

    def test_rectangle8(self):
        """
        validate the type of arguments height and width
        """
        with self.assertRaises(TypeError):
            R13 = Rectangle("Holberton", 7)
        with self.assertRaises(TypeError):
            R14 = Rectangle(5, "Betty")
        with self.assertRaises(TypeError):
            R15 = Rectangle((4, 8), 2)
        with self.assertRaises(TypeError):
            R16 = Rectangle(6, [2, 5])
        with self.assertRaises(TypeError):
            R17 = Rectangle({"KEY": 10}, 4)

    def test_rectangle9(self):
        """
        validate the type of arguments x and y
        """
        with self.assertRaises(TypeError):
            R18 = Rectangle(4, 8, 1, "Holbie")
        with self.assertRaises(TypeError):
            R19 = Rectangle(4, 8, [10, 4], 10)
        with self.assertRaises(TypeError):
            R20 = Rectangle(4, 8, 1, (12, 20))
        with self.assertRaises(TypeError):
            R21 = Rectangle(4, 8, 1, {10: 2})

    def test_rectangle10(self):
        """
        Validate the size of width
        """
        with self.assertRaises(ValueError):
            Rectangle(-2, 6)

    def test_rectangle11(self):
        """
        Validate the size of height
        """
        with self.assertRaises(ValueError):
            Rectangle(5, -2)

    def test_rectangle12(self):
        """
        validate the position of x and y
        """
        with self.assertRaises(ValueError):
            Rectangle(5, 4, -1, 3)
        with self.assertRaises(ValueError):
            Rectangle(5, 4, 1, -3)

    def test_rectangle13(self):
        """
        Test the area of Rectangle
        """
        R22 = Rectangle(2, 5)
        self.assertEqual(R22.area(), 10)
        R23 = Rectangle(2, 4, 2, 1, 6)
        self.assertEqual(R23.area(), 8)

    def test_rectangle14(self):
        """
        Test str of Rectangle
        """
        R24 = Rectangle(6, 3, 1, 4, 8)
        self.assertEqual(R24.__str__(), "[Rectangle] (8) 1/4 - 6/3")

    def test_rectangle15(self):
        """
        Test display the rectangle
        """
        pass

    def test_rectangle16(self):
        """
        Test update of rectangle TEST: ID
        """
        R25 = Rectangle(4, 8, 1, 3, 10)
        self.assertEqual(R25.__str__(), "[Rectangle] (10) 1/3 - 4/8")
        R25.update(24)
        self.assertEqual(R25.__str__(), "[Rectangle] (24) 1/3 - 4/8")

    def test_rectangle17(self):
        """
        Test update of rectangle TEST:WIDTH
        """
        R26 = Rectangle(4, 8, 1, 3, 10)
        self.assertEqual(R26.__str__(), "[Rectangle] (10) 1/3 - 4/8")
        R26.update(24, 5)
        self.assertEqual(R26.__str__(), "[Rectangle] (24) 1/3 - 5/8")

    def test_rectangle18(self):
        """
        Test update of rectangle TEST:HEIGHT
        """
        R27 = Rectangle(4, 8, 1, 3, 10)
        self.assertEqual(R27.__str__(), "[Rectangle] (10) 1/3 - 4/8")
        R27.update(24, 5, 7)
        self.assertEqual(R27.__str__(), "[Rectangle] (24) 1/3 - 5/7")

    def test_rectangle19(self):
        """
        Test update of rectangle TEST:X
        """
        R28 = Rectangle(4, 8, 1, 3, 10)
        self.assertEqual(R28.__str__(), "[Rectangle] (10) 1/3 - 4/8")
        R28.update(24, 5, 7, 0)
        self.assertEqual(R28.__str__(), "[Rectangle] (24) 0/3 - 5/7")

    def test_rectangle20(self):
        """
        Test update of rectangle TEST:Y
        """
        R29 = Rectangle(4, 8, 1, 3, 10)
        self.assertEqual(R29.__str__(), "[Rectangle] (10) 1/3 - 4/8")
        R29.update(24, 5, 7, 0, 4)
        self.assertEqual(R29.__str__(), "[Rectangle] (24) 0/4 - 5/7")

    def test_rectangle21(self):
        """
        Test update with invalid value
        """
        R30 = Rectangle(8, 4, 3, 2, 1)
        self.assertEqual(R30.__str__(), "[Rectangle] (1) 3/2 - 8/4")
        with self.assertRaises(ValueError):
            R30.update(24, -5)

    def test_rectangle22(self):
        """
        Test update with type str in id
        """
        R31 = Rectangle(8, 4, 3, 2, 1)
        self.assertEqual(R31.__str__(), "[Rectangle] (1) 3/2 - 8/4")
        R31.update("Holberton", 3)
        self.assertEqual(R31.__str__(), "[Rectangle] (Holberton) 3/2 - 3/4")

    def test_rectangle23(self):
        """
        Test update with type str in id
        """
        R32 = Rectangle(8, 4, 3, 2, 1)
        self.assertEqual(R32.__str__(), "[Rectangle] (1) 3/2 - 8/4")
        with self.assertRaises(TypeError):
            R32.update(10, "holberton")

    def test_rectangle24(self):
        """
        test display rectangle
        """
        R33 = Rectangle(2, 2)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        R33.display()
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(output, '##\n##\n')

    def test_rectangle25(self):
        """
        test display #1
        """
        R34 = Rectangle(2, 3, 2, 2)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        R34.display()
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(output, '\n' * 2 + (' ' * 2 + '#' * 2 + '\n') * 3)

    def test_rectangle26(self):
        """
        Test update of rectangle with **kwargs
        """
        R35 = Rectangle(4, 8, 1, 3, 10)
        self.assertEqual(R35.__str__(), "[Rectangle] (10) 1/3 - 4/8")
        R35.update(height=1)
        self.assertEqual(R35.__str__(), "[Rectangle] (10) 1/3 - 4/1")
        R35.update(width=1, x=2)
        self.assertEqual(R35.__str__(), "[Rectangle] (10) 2/3 - 1/1")
        R35.update(y=1, width=2, x=3, id=89)
        self.assertEqual(R35.__str__(), "[Rectangle] (89) 3/1 - 2/1")
        R35.update(x=1, height=2, y=2, width=5)
        self.assertEqual(R35.__str__(), "[Rectangle] (89) 1/2 - 5/2")

    def test_rectangle27(self):
        """
        Test Rectangle Return a Dictionary
        """
        R36 = Rectangle(10, 2, 1, 9, 11)
        self.assertEqual(R36.__str__(), "[Rectangle] (11) 1/9 - 10/2")
        R36_dictionary = R36.to_dictionary()
        dicts = {'x': 1, 'y': 9, 'id': 11, 'height': 2, 'width': 10}
        self.assertEqual(R36.to_dictionary(), dicts)

if __name__ == "__main__":
    unittest.main()
