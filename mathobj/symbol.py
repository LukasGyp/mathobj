from mathobj.expr import Expr

class Symbol:
    def __init__(self, symbol):
        self._symbol = str(symbol)

    def __str__(self):
        return self._symbol

    def __add__(self, expr):
        return Expr(f'{self} + {expr}')

    def __sub__(self, expr):
        return Expr(f'{self} - {expr}')

    def __mul__(self, expr):
        return Expr(f'{self}{expr}')
