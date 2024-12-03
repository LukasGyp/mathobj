from mathobj.symbol import Symbol
from mathobj.expr import Expr

def test_str_01():
    a = Expr('a')
    assert str(a) == 'a'

def test_add_01():
    a = Symbol('a')
    b = Symbol('b')
    assert str(a+b) == 'a + b'

def test_add_02():
    x = Symbol('x')
    y = Symbol('y')
    im_f = Symbol('Im(f)')
    assert str(x + y + im_f) == 'x + y + Im(f)'

def test_sub_01():
    a = Symbol('a')
    b = Symbol('b')
    assert str(a-b) == 'a - b'

def test_sub_02():
    x = Symbol('x')
    y = Symbol('y')
    im_f = Symbol('Im(f)')
    assert str(x - y - im_f) == 'x - y - Im(f)'
    
def test_mul_01():
    a = Symbol('a')
    b = Symbol('b')
    assert str(a*b) == 'ab'

def test_mul_02():
    x = Symbol('x')
    y = Symbol('y')
    im_f = Symbol('Im(f)')
    assert str(x * y * im_f) == 'xyIm(f)'
    
    
