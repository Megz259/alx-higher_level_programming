#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.square import Square

class TestBase_update(unittest.TestCase):
    """Test base class created"""

    def test_update_rectangle_start(self):
        r1 = Rectangle(4, 6, 1, 3, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/3 - 4/6", str(r1))

    def test_update_rectangle_a(self):
        r1 = Rectangle(4, 6, 1, 3, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/3 - 4/6", str(r2))

    def test_update_rectangle_b(self):
        r1 = Rectangle(4, 6, 1, 3, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_update_rectangle_c(self):
        r1 = Rectangle(4, 6, 1, 3, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_update_square_d(self):
        s1 = Square(4, 6, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 6/1 - 4", str(s1))

    def test_update_square_a(self):
        s1 = Square(4, 6, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 6/1 - 4", str(s2))

    def test_update_square_b(self):
        s1 = Square(4, 6, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_update_square_c(self):
        s1 = Square(4, 6, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


if __name__ == "__main__":
    unittest.main()
