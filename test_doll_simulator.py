import unittest
from exceptions import *
from square_table import SquareTable
from doll import Doll


class TestDollSimulator(unittest.TestCase):

    def setUp(self):
        self.table = SquareTable(5)
        self.doll = Doll(self.table)

    def test_ignore_cmd_before_place_move(self):
        with self.assertRaises(PlaceNotExecuted):
            self.doll.move()

    def test_ignore_cmd_before_place_left(self):
        with self.assertRaises(PlaceNotExecuted):
            self.doll.left()

    def test_ignore_cmd_before_place_right(self):
        with self.assertRaises(PlaceNotExecuted):
            self.doll.right()

    def test_boundary_limit_place(self):
        with self.assertRaises(BoundException):
            self.doll.place([6,6,"NORTH"])

    def test_boundary_limit_move(self):
        with self.assertRaises(BoundException):
            self.doll.place([2, 3, "NORTH"])
            self.doll.move()
            self.doll.move()

    def test_positive_move(self):
        self.doll.place([2, 3, "NORTH"])
        self.doll.move()
        self.assertEqual(self.doll.position.x,2)
        self.assertEqual(self.doll.position.y, 4)

    def test_positive_turn(self):
        self.doll.place([2, 3, "EAST"])
        self.doll.left()
        self.assertEqual(self.doll.direction,"NORTH")
        self.doll.left()
        self.assertEqual(self.doll.direction,"WEST")

    def test_positive_turn_move(self):
        self.doll.place([2, 3, "NORTH"])
        self.doll.left()
        self.assertEqual(self.doll.direction, "WEST")
        self.doll.move()
        self.assertEqual(self.doll.direction, "WEST")
        self.assertEqual(self.doll.position.x, 1)
        self.assertEqual(self.doll.position.y, 3)


if __name__ == '__main__':
    unittest.main()
