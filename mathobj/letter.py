from mathobj.expr import Expr

class Letter:
    def __init__(self, letter):
        self._letter = str(letter)

    def __str__(self):
        return self._letter

    def __repr__(self):
        return self._letter

    def __add__(self, other):
        if isinstance(other, Letter):
            other = Expr([other])
        return Expr([self]) + other

    def __sub__(self, other):
        if isinstance(other, Letter):
            other = Expr([other])
        return Expr([self]) - other

    def __mul__(self, other):
        if isinstance(other, Letter):
            other = Expr([other])
        return Expr([self]) * other
