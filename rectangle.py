class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, top_left, top_right, bottom_right, bottom_left, name):
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_right = bottom_right
        self.bottom_left = bottom_left
        self.name = name

    def intersects(self, other):
        # return not (self.top_right.x < other.bottom_left.x or self.bottom_left.x > other.top_right.x or self.top_right.y < other.bottom_left.y or self.bottom_left.y > other.top_right.y)
        pass