from mlproject.distance import haversine
def test_dist0():
    assert haversine(10,40,10,40) == 0
