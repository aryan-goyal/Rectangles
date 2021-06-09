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
    top_left = Point(points[0]['x'], points[1]['y'])
    top_right = Point(points[1]['x'], points[1]['y'])
    bottom_right = Point(points[1]['x'], points[0]['y'])
    bottom_left = Point(points[0]['x'], points[0]['y'])
    return Rectangle(top_left, top_right, bottom_right, bottom_left, name)

def validate_rect(rect):
    points = rect['points']
    err_msg = "Error: {} contains invalid points!".format(rect['name'])
    #assert that top right point is greater than bottom left point in x and y
    assert points[0]['x'] < points[1]['x'] and points[0]['y'] < points[1]['y'], err_msg
    return True
  
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
            aggregate_rectangles = []
            for rect in rectangles:
                aggregate_rectangles.append(generate_rectangle(rect['points'], rect['name']))

            print(aggregate_rectangles)