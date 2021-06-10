import json
import sys
from point import Point
from rectangle import Rectangle

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as  MatRectangle

def read_json(file_name):
    """
    :type file_name: str
    :rtype: dict
    """
    f = open(file_name,)
    data = json.load(f)
    f.close()
    return data

def generate_rectangle(points, name):
    """
    :type points: dict, name: str
    :rtype: Rectangle
    """
    top_left = Point(points[0][0], points[1][1])
    top_right = Point(points[1][0], points[1][1])
    bottom_right = Point(points[1][0], points[0][1])
    bottom_left = Point(points[0][0], points[0][1])

    try:
        return Rectangle(top_left, top_right, bottom_right, bottom_left, name)
    except Exception as e:
        print('{errors: ["Unable to generate rectangle"], exception: ', e, '}')

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
    :rtype: bool
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

def show_rectangles(rectangles, filepath):
    """
    :type rect: list, filename: str
    :rtype: None
    """
    fig, ax = plt.subplots()
    max_workspace = 0
    for rect in rectangles:
        width = rect.width()
        height = rect.height()
        max_workspace = max(max_workspace, width, height)
        ax.add_patch(MatRectangle((rect.bottom_left.x, rect.bottom_left.y), width, height, fill=False))
    
    ax.plot([0, max_workspace+5],[0, max_workspace+5], linestyle='none')
    # plt.show()
    
    try:
        filename = "figures/" + filepath.rsplit('/',1)[1].rsplit('.',1)[0] +".png"
        plt.savefig(filename)
    except Exception as e:
        print('{errors: ["Unable to save figure"], exception: ', e, '}')

def detectFeatures(self, other):
    pass

if __name__ == "__main__":
    filepath = sys.argv[1]
    data = read_json(filepath)

    rectangles = []
    if data:
        rectangles = get_rectangles(data)
        # print(rectangles[0])
        # print(rectangles[1])
        print(rectangles[0].adjacentProper(rectangles[1]))
        

        # show_rectangles(rectangles, filepath)