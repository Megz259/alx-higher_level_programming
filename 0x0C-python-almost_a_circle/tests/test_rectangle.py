#!/usr/bin/python3
"""Test for rectangle"""
import io
import sys
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestTheRectangle(unittest.TestCase):
    """Testing the class creation"""

    def test_rectangle_creation(self):
        Base._Base__nb_objects = 0

    def reset(self):
        """reset"""
        pass

    def test_none(self):
        """test class type"""
        with self.assertRaise(TypeError):
            Rectangle()

    def test_base(self):
        """test class type"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_one(self):
        """Test for 1 arg"""
        with self.assertRaise(TypeError):
            Rectangle(1)

    def test_many(self):
        """test for many arguments"""
        with self.assertRaise(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5, 6)
            s = "__init__() arguments given"
            self.assertEqual(str(e.exception), s)

    def test_creation(self):
        """testing code"""
        r = Rectangle(20, 40)
        self.assertEqual(str(type(r)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(r, Base))
        d = {"_Rectangle__height": 40, "_Rectangle__width": 20,
                "_Rectangle__x": 0, "_Rectangle__y": 0, "id": 1}
        self.assertDictEqual(r.__dict__, d)

        with self.assertRaise(TypeError) as e:
            r = Rectangle(1, "2")
            response = "height must be an integer"
            self.assertEqual(str(e.exception), response)

        with self.assertRaise(TypeError) as e:
            r = Rectangle("1", 2)
            response = "width must be an integer"
            self.assertEqual(str(e.exception), response)

        with self.assertRaise(TypeError) as e:
            r = Rectangle(1, 2, "3")
            response = "x must be an integer"
            self.assertEqual(str(e.exception), response)

        with self.assertRaise(TypeError) as e:
            r = Rectangle(1, 2, 3, "4")
            response = "y must be an integer"
            self.assertEqual(str(e.exception), response)

        with self.assertRaise(TypeError) as e:
            r = Rectangle(1, -2)
            response = "height must be > 0"
            self.assertEqual(str(e.exception), response)

        with self.assertRaise(TypeError) as e:
            r = Rectangle(1, 0)
            response = "height must be > 0"
            self.assertEqual(str(e.exception), response)

        with self.assertRaise(TypeError) as e:
            r = Rectangle(-1, 2)
            response = "width must be > 0"
            self.assertEqual(str(e.exception), response)

        with self.assertRaise(TypeError) as e:
            r = Rectangle(0, 2)
            response = "width must be > 0"
            self.assertEqual(str(e.exception), response)

        with self.assertRaise(TypeError) as e:
            r = Rectangle(1, 2, -3)
            response = "x must be >= 0"
            self.assertEqual(str(e.exception), response)

        with self.assertRaise(TypeError) as e:
            r = Rectangle(1, 2, 3, -4)
            response = "y must be >= 0"
            self.assertEqual(str(e.exception), response)

    def test_creation_place(self):
        """testing code"""
        r = Rectangle(20, 40, 25, 45)
        d = {"_Rectangle__height": 40, "_Rectangle__width": 20,
                "_Rectangle__x": 25, "_Rectangle__y": 45, "id": 1}
        self.assertEqual(r.__dict__, d)

    def test_creation_place(self):
        """testing code"""
        r = Rectangle(20, 40, 25, 45, 90)
        d = {"_Rectangle__height": 40, "_Rectangle__width": 20,
                "_Rectangle__x": 25, "_Rectangle__y": 45, "id": 90}
        self.assertEqual(r.__dict__, d)

    def test_creation_place(self):
        """testing code"""
        r = Rectangle(20, 40, x=25, id=90, y=45)
        d = {"_Rectangle__height": 40, "_Rectangle__width": 20,
                "_Rectangle__x": 25, "_Rectangle__y": 45, "id": 90}
        self.assertEqual(r.__dict__, d)
