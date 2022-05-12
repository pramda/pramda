from functions import any


def test_answer():
    assert any(lambda x: x == 1, [1, 2, 3]) == True
    assert any(lambda x: x == 10, [1, 2, 3]) == False
    assert any(lambda x: x == 1)([1, 2, 3]) == True
    assert any(lambda x: x == 10)([1, 2, 3]) == False
