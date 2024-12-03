from mathobj.letter import Letter
from mathobj.expr import Expr

def test_str_01():
    a = Expr('a')
    assert str(a) == 'a'

def test_add_01():
    a = Letter('a')
    b = Letter('b')
    assert str(a+b) == 'a + b'

def test_add_02():
    x = Letter('x')
    y = Letter('y')
    im_f = Letter('Im(f)')
    assert str(x + y + im_f) == 'x + y + Im(f)'

def test_add_03():
    x = Letter('x')
    assert str(x + 2) == 'x + 2'

def test_sub_01():
    a = Letter('a')
    b = Letter('b')
    assert str(a-b) == 'a - b'

def test_sub_02():
    x = Letter('x')
    y = Letter('y')
    im_f = Letter('Im(f)')
    assert str(x - y - im_f) == 'x - y - Im(f)'
    
def test_mul_01():
    a = Letter('a')
    b = Letter('b')
    assert str(a*b) == 'ab'

def test_mul_02():
    x = Letter('x')
    y = Letter('y')
    im_f = Letter('Im(f)')
    assert str(x * y * im_f) == 'xyIm(f)'
    
    
