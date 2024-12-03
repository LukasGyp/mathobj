from mathobj.symbol import Symbol

class Expr:
    """
    list of letters and symbols
    """
    def __init__(self, list_):
        self._expr = list_

    def __str__(self):
        return ''.join(map(str, self._expr))

    def __repr__(self):
        return ''.join(map(repr, self._expr))

    def __add__(self, other):
        if not isinstance(other, Symbol):
            other = Expr([other])
        return Expr(self._expr + [Symbol(' + ')] + other._expr)

    def __sub__(self, other):
        if not isinstance(other, Symbol):
            other = Expr([other])
        return Expr(self._expr + [Symbol(' - ')] + other._expr)

    def __mul__(self, other):
        if not isinstance(other, Symbol):
            other = Expr([other])
        return Expr(self._expr + other._expr)
