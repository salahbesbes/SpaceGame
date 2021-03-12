#!/usr/bin/python3
from Classes import Player
from io import StringIO
from unittest.mock import patch
import unittest


class TestBase(unittest.TestCase):
    def test_img(self):
        player = Player('../ufo.png', 0, 0)
        player.x = 0

        with self.assertRaises(TypeError) as msg:
            player = Player(5.6, 1, 9)
        self.assertEqual(str(msg.exception), "pls give me the path of the img")

        with self.assertRaises(FileNotFoundError):
            player = Player("ufo.png", 5, 0)

        with self.assertRaises(TypeError) as msg:
            player = Player(True, 5, 0)
        self.assertEqual(str(msg.exception), "pls give me the path of the img")

        with self.assertRaises(ValueError) as msg:
            player = Player("../ufo.png", -5, 0)
        self.assertEqual(str(msg.exception), "out of limit pls check X or Y")

        with self.assertRaises(ValueError) as msg:
            player = Player("ufo.png", -5, 0)
        self.assertEqual(str(msg.exception), "out of limit pls check X or Y")

