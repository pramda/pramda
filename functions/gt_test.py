from .gt import gt

def test_answer():
    assert(gt(1,2)) == False
    assert(gt(2,2)) == False
    assert(gt(2.1,2)) == True
    assert(gt(3, 2)) == True