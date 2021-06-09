import json
import sys
from rectangle import Point
from rectangle import Rectangle

def read_json(file_name):
    f = open(file_name,)
    data = json.load(f)
    f.close()
    return data

def generate_rectangle(points, name):
    top_left = Point(points[0][0], points[1][1])
    top_right = Point(points[1][0], points[1][1])
    bottom_right = Point(points[1][0], points[0][1])
    bottom_left = Point(points[0][0], points[0][1])
    return Rectangle(top_left, top_right, bottom_right, bottom_left, name)

def validate_rect(rect):
    points = rect['points']
    err_msg = "Error: {} contains invalid points!".format(rect['name'])
    #assert that top right point is greater than bottom left point in x and y
    assert points[0][0] < points[1][0] and points[0][1] < points[1][1], err_msg
  
def validate_json(rectangles):
    valid = True
    for rect in rectangles:
        try:
            validate_rect(rect)
        except Exception as e:
            print('{errors: ["JSON contains invalid rectangles"], exception: ', e, '}')
            valid = False
    return valid

if __name__ == "__main__":
    data = read_json(sys.argv[1])

    if data:
        rectangles = data['rectangles']
        if validate_json(rectangles):
            all_rectangles = []
            for rect in rectangles:
                all_rectangles.append(generate_rectangle(rect['points'], rect['name']))
            
            for x in all_rectangles:
                print(x)   