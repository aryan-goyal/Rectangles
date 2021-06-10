class Point:
    def __init__(self, x=0.0, y=0.0):
        """
        :type x: float
        :rtype: none
        """
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def __eq__(self, other): 
        """
        :type x: Point
        :rtype: bool
        """
        if not isinstance(other, Point):
            # should not compare against unrelated types
            return NotImplemented

        return self.x == other.x and self.y == other.y