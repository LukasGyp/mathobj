class Set:
    def __init__(self, dfn):
        if callable(dfn):
            self.indicator = dfn
        elif isinstance(dfn, list):
            self.indicator = self._list_indicator

    def _list_indicator(self, lst):
        def indicator(x):
            return x in lst
        return indicator

    def __contains__(self, x):
        return self.indicator(x)

    def __or__(self, other):
        return self.indicator | other.indicator
