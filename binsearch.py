import bisect

__version__ = '0.1'

class BinSearch:

    def __init__(self, items, sort=False):
        if isinstance(items, dict):
            self.items = list(items.items())
            sort = True
        else:
            self.items = items
        if sort:
            self.items.sort()
        self.bounds = [s[0] for s in self.items[1:]]

    def find(self, value):  
        return self.items[bisect.bisect(self.bounds, value)]

    def __call__(self, value):
        return self.find(value)[1]

