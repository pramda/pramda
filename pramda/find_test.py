from .find import find


def test_find():
    assert find(lambda x: x > 2, [1, 2, 3, 4]) == 3
    assert find(lambda x: x == 5, [1, 2, 3, 4]) is None
    assert find(lambda x: x % 2 == 0, [1, 3, 5, 7]) is None
    assert find(lambda x: x < 0, [-3, -2, -1, 0, 1]) == -3
    assert find(lambda x: x == "apple", ["banana", "apple", "orange"]) == "apple"
    assert find(lambda x: x["id"] == 2, [{"id": 1}, {"id": 2}, {"id": 3}]) == {"id": 2}
    assert find(lambda x: x is None, [1, 2, None, 4]) is None
