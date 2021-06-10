from run import detect_features, get_rectangles, read_json

def test_containment():
    feature = detect_features(get_rectangles(read_json("tests/containment.json")))
    assert feature == '{"rectangle1": "rectangle2", "feature": "Containment"}'

def test_intersection():
    feature = detect_features(get_rectangles(read_json("tests/intersection.json")))
    assert feature == '{"rectangle1": "rectangle2", "feature": "Intersects"}'

def test_no_intersection_Adjacent_containment():
    feature = detect_features(get_rectangles(read_json("tests/noIntersectionAdjacentContainment.json")))
    assert feature == '{"rectangle1": "rectangle2", "feature": "No Features Found"}'

def test_adjacent_partial():
    feature = detect_features(get_rectangles(read_json("tests/adjacentPartial.json")))
    assert feature == '{"rectangle1": "rectangle2", "feature": "Adjacent (Partial)"}'

def test_adjacent_proper():
    feature = detect_features(get_rectangles(read_json("tests/adjacentProper.json")))
    assert feature == '{"rectangle1": "rectangle2", "feature": "Adjacent (Proper)"}'

def test_adjacent_subline():
    feature = detect_features(get_rectangles(read_json("tests/adjacentSubline.json")))
    assert feature == '{"rectangle1": "rectangle2", "feature": "Adjacent (Sub-line)"}'

def test_invalid_rectangle():
    rectangles = get_rectangles(read_json("tests/invalidRectangle.json"))
    assert rectangles == None