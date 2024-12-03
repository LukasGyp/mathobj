from mathobj.set import Set

def test_contain_01():
    X = Set([1, 2, 3])
    assert 1 in X
    assert 2 in X
    assert 3 in X

def test_contain_02():
    x = Set(lambda x: x<1)
    assert -1 in x
    assert 0 in x
    assert 1 not in x
    assert 2 not in x

def test_union_01():
    assert Set([1, 2, 3]) | Set([4, 5, 6]) == Set([1, 2, 3, 4, 5, 6])

def test_union_02():
    assert Set([1, 2, 3]) | Set([3, 4, 5]) == Set([1, 2, 3, 4, 5])

def test_union_03():
    assert Set(lambda x: x<1) | Set(lambda x: x>2) == Set(lambda x: (x < 1 and x > 2))
