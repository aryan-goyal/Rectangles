class Rectangle:
    def __init__(self, top_left, top_right, bottom_right, bottom_left, name):
        """
        :type top_left: Point, top_right: Point, bottom_right: Point, bottom_left: Point, name: string
        :rtype: none
        """
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_right = bottom_right
        self.bottom_left = bottom_left
        self.name = name

    def __str__(self):
        return "{},[[{},{}],[{},{}]]".format(self.name, str(self.top_left), str(self.top_right), str(self.bottom_right), str(self.bottom_left))

    def width(self):
        """
        :rtype: bool
        """
        return self.top_right.x - self.top_left.x

    def height(self):
        """
        :rtype: bool
        """
        return self.top_left.y - self.bottom_left.y
        
    def intersects(self, other):
        """
        :type other: Rectangle
        :rtype: bool
        """
        #collision detection using Separating Axis Theorem, if opposite corners pass through each other then intersect
        return not (self.top_right.x <= other.bottom_left.x or self.bottom_left.x >= other.top_right.x or \
                    self.top_right.y <= other.bottom_left.y or self.bottom_left.y >= other.top_right.y)

    def adjacent_proper(self, other):
        """
        :type other: Rectangle
        :rtype: bool
        """
        #compare corners
        #adjacent proper top
        adjacent_top = self.top_left == other.bottom_left and self.top_right == other.bottom_right

        #adjacent proper bottom
        adjacent_bottom = self.bottom_left == other.top_left and self.bottom_right == other.top_right

        #adjacent proper left
        adjacent_left = self.top_left == other.top_right and self.bottom_left == other.bottom_right

        #adjacent proper right
        adjacent_right = self.top_right == other.top_left and self.bottom_right == other.bottom_left
        
        return adjacent_top or adjacent_bottom or adjacent_left or adjacent_right

    def adjacent_partial(self, other):
        """
        :type other: Rectangle
        :rtype: bool
        """
        #adjacent partial top
        adjacent_top = self.top_left.x < other.bottom_right.x and self.top_left.x > other.bottom_left.x and self.top_left.y == other.bottom_right.y or \
                    self.top_right.x > other.bottom_left.x and self.top_right.x < other.bottom_right.x and self.top_left.y == other.bottom_right.y
        
        #adjacent partial bottom
        adjacent_bottom = self.bottom_left.x < other.top_right.x and self.bottom_left.x > other.top_left.x and self.bottom_left.y == other.top_left.y or \
                    self.bottom_right.x > other.top_left.x and self.bottom_right.x < other.top_right.x and self.bottom_right.y == other.top_right.y   
        
        #adjacent partial left
        adjacent_left = self.top_left.x == other.top_right.x and self.top_left.y < other.top_right.y and self.top_left.y > other.bottom_right.y or \
                    self.bottom_left.x == other.top_right.x and self.bottom_left.y < other.top_right.y and self.bottom_left.y > other.bottom_right.y   
        
        #adjacent partial right
        adjacent_right = self.top_right.x == other.top_left.x and self.top_right.y < other.top_left.y and self.top_right.y > other.bottom_left.y or \
                    self.bottom_right.x == other.top_left.x and self.bottom_right.y < other.top_left.y and self.bottom_right.y > other.bottom_left.y   
        
        return adjacent_top or adjacent_bottom or adjacent_left or adjacent_right

    def adjacent_subline(self, other):
        """
        :type other: Rectangle
        :rtype: bool
        """
        #adjacent subline top
        adjacent_top = self.top_left.x < other.bottom_left.x and self.top_left.y == other.bottom_left.y and self.top_right.x > other.bottom_right.x
        
        #adjacent subline bottom
        adjacent_bottom = self.bottom_left.x < other.top_left.x and self.bottom_left.y == other.top_left.y and self.bottom_right.x > other.top_right.x
        
        #adjacent subline left
        adjacent_left = self.top_left.x == other.top_right.x and self.top_left.y > other.top_right.y and self.bottom_left.y < other.bottom_right.y
        
        #adjacent subline right
        adjacent_right = self.top_right.x == other.top_left.x and self.top_right.y > other.top_left.y and self.bottom_right.y < other.bottom_left.y
        
        return adjacent_top or adjacent_bottom or adjacent_left or adjacent_right

    def contains(self, other):
        """
        :type other: Rectangle
        :rtype: bool
        """
        # If top-right inner box corner is inside the the containing box and If bottom-left inner box corner is inside the containg box
        return self.top_right.x > other.top_right.x and self.top_right.y > other.top_right.y \
             and self.bottom_left.x < other.bottom_left.x and self.bottom_left.y < other.bottom_left.y