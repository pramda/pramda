from .pick import pick

def test_pick():
    assert pick(['a', 'c'], {'a': 1, 'b': 2, 'c': 3}) == {'a': 1, 'c': 3}
    
    assert pick(['a!', 'c#'], {'a!': 1, 'b@': 2, 'c#': 3}) == {'a!': 1, 'c#': 3}
    
    assert pick([], {'a': 1, 'b': 2, 'c': 3}) == {}
