class Symbol:
    def __init__(self, symbol):
        self._symbol = str(symbol)

    def __str__(self):
        return self._symbol

    def __repr__(self):
        return self._symbol
