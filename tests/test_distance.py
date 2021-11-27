from mstoolbox.distance import haversine

def test_type_of_haversineDistance():
    """checks that function returns a float"""
    assert type(haversine(1,2,3,4)) == type(1.0)

def test_distance_of_haversineDistance():
    """checks that function returns a non-zero number"""
    assert haversine(1,2,3,4) != 0