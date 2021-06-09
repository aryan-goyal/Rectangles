import json
import sys
from rectangle import Point
from rectangle import Rectangle

def read_json(file_name):
    """
    :type file_name: string
    :rtype: dict
    """
    f = open(file_name,)
    data = json.load(f)
    f.close()
    return data

def generate_rectangle(points, name):
    """
    :type points: dict, name: string
    :rtype: Rectangle
    """
    top_left = Point(points[0][0], points[1][1])
    top_right = Point(points[1][0], points[1][1])
    bottom_right = Point(points[1][0], points[0][1])
    bottom_left = Point(points[0][0], points[0][1])
    return Rectangle(top_left, top_right, bottom_right, bottom_left, name)

def validate_rect(rect):
    """
    :type rect: dict
    :rtype: None
    """
    points = rect['points']
    err_msg = "Error: {} contains invalid points!".format(rect['name'])
    #assert that top right point is greater than bottom left point in x and y
    assert points[0][0] < points[1][0] and points[0][1] < points[1][1], err_msg
  
def validate_json(rectangles):
    """
    :type rect: dict
    :rtype: boolean
    """
    valid = True
    for rect in rectangles:
        try:
            validate_rect(rect)
        except Exception as e:
            print('{errors: ["JSON contains invalid rectangles"], exception: ', e, '}')
            valid = False
    return valid

def get_rectangles(data):
    """
    :type rect: dict
    :rtype: list
    """
    rectangles = data['rectangles']
    if validate_json(rectangles):
        aggr = []
        for rect in rectangles:
            aggr.append(generate_rectangle(rect['points'], rect['name']))
    
        return aggr


if __name__ == "__main__":
    data = read_json(sys.argv[1])

    if data:
        rectangles = get_rectangles(data)

        for x in rectangles:
            print(x.width(), x.height())