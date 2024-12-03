class Function:
    def __init__(self, f):
        self._f = f

    def __call__(self, x):
        return self._f(x)

    def __matmul__(self, other):
        def composed_func(x):
            return self._f(other._f(x))
        return Function(composed_func)
