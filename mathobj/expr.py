class Expr:
    def __init__(self, expr):
        self._expr = str(expr)

    def __str__(self):
        return self._expr

    def __add__(self, expr):
        return Expr(f'{self} + {expr}')

    def __sub__(self, expr):
        return Expr(f'{self} - {expr}')

    def __mul__(self, expr):
        return Expr(f'{self}{expr}')
