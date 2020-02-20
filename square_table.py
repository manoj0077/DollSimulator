from grid import Point


class SquareTable(object):

    def __init__(self, length):
        self.south_west = Point(0,0)
        self.north_east = Point(length-1,length-1)

    def contains(self, point):
        return self.south_west <= point and self.north_east >= point