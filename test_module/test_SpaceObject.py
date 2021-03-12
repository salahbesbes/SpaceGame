#!/usr/bin/python3
from Classes import SpaceObject
from io import StringIO
from unittest.mock import patch
import unittest


class TestBase(unittest.TestCase):
    def test_coordinate(self):
        """ test """
        b1 = SpaceObject(0, 0)
        self.assertEqual(b1.x, 0)
        self.assertEqual(b1.y, 0)
        b2 = SpaceObject(50, 60)
        self.assertEqual(b2.x, 50)
        self.assertEqual(b2.y, 60)

        with self.assertRaises(ValueError) as msg:
            b3 = SpaceObject(50000, 60)
        self.assertEqual(str(msg.exception), "out of limit pls check X or Y")
        with self.assertRaises(ValueError) as msg:
            b4 = SpaceObject(55, -5)
        self.assertEqual(str(msg.exception), "out of limit pls check X or Y")

        with self.assertRaises(TypeError) as msg:
            b5 = SpaceObject("50000", 60)
        self.assertEqual(str(msg.exception), "X and Y must be positive integers")
        with self.assertRaises(TypeError) as msg:
            b6 = SpaceObject(55, "66666666")
        self.assertEqual(str(msg.exception), "X and Y must be positive integers")

    def test_screen(self):
        b1 = SpaceObject(0, 0)
        self.assertEqual(SpaceObject.sc_width, 800)
        self.assertEqual(SpaceObject.sc_height, 600)
        b1 = SpaceObject(55, 66, 200, 300)
        self.assertEqual(SpaceObject.sc_width, 200)
        self.assertEqual(SpaceObject.sc_height, 300)

        with self.assertRaises(ValueError):
            b3 = SpaceObject(50, 60, 0, -5)
        with self.assertRaises(ValueError):
            b4 = SpaceObject(55, -5, 555555, 444)

        with self.assertRaises(TypeError) as msg:
            b5 = SpaceObject(5, 60, 900, None)
        self.assertEqual(str(msg.exception), "width and height must be positive integers")
        with self.assertRaises(TypeError) as msg:
            b6 = SpaceObject(55, 66, "ddd", 500)
        self.assertEqual(str(msg.exception), "width and height must be positive integers")
