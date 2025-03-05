from .omit import omit

def test_omit():
    assert omit(['b'], {'a': 1, 'b': 2, 'c': 3}) == {'a': 1, 'c': 3}
    
    assert omit(['b@'], {'a!': 1, 'b@': 2, 'c#': 3}) == {'a!': 1, 'c#': 3}
    
    assert omit([], {'a': 1, 'b': 2, 'c': 3}) == {'a': 1, 'b': 2, 'c': 3}

