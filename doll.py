from grid import Point, Direction
from exceptions import *


class Doll():
    def __init__(self, table):
        self.table = table
        self.position = None
        self.direction = None
        self.dirs = ["NORTH", "EAST", "SOUTH", "WEST"]
        self.arrow = {
            "NORTH": Direction(0, 1),
            "EAST": Direction(1, 0),
            "SOUTH": Direction(0, -1),
            "WEST": Direction(-1, 0),
        }

    def place(self, params):
        position = Point(int(params[0]),int(params[1]))
        if self.table.contains(position):
            self.position = position
            if params[2] in self.dirs:
                self.direction = params[2]
            else:
                raise NotValidCommand('Command Not in Proper Format: "%s"' % params[2])
        else:
            raise BoundException('Given Position Not on Table')

    def move(self):
        if not self.position:
            raise PlaceNotExecuted('PLACE command is Not Executed Till Now')
        new_pos = self.position + (self.arrow[self.direction] * 1)
        if self.table.contains(new_pos):
            self.position = new_pos
        else:
            raise BoundException('Cannot Move the Doll Beyond Boundaries')

    def left(self):
        if self.position is None:
            raise PlaceNotExecuted('PLACE command is Not Executed Till Now')
        pos = self.dirs.index(self.direction)
        pos_new = (pos - 1) % len(self.dirs)
        new_dir = self.dirs[pos_new]
        self.direction = new_dir

    def right(self):
        if self.position is None:
            raise PlaceNotExecuted('PLACE command is Not Executed Till Now')
        pos = self.dirs.index(self.direction)
        pos_new = (pos + 1) % len(self.dirs)
        new_dir = self.dirs[pos_new]
        self.direction = new_dir

    def report(self):
        if self.position is None:
            raise PlaceNotExecuted('PLACE command is Not Executed Till Now')
        print(self.position.x,self.position.y,self.direction)