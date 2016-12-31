import pickle
import inspect
import os

class Saver():
    def __init__(self):
        self.ignoresaves = False

    def ignore(self, b = True):
        self.ignoresaves = b

    def save(self, name, obj):
        filename = "__cache__/" + inspect.stack()[1][1] + "_name"
        with open(filename, 'wb') as f:
            pickle.dump(obj, f)

    def load(self, obj):
        if self.ignoresaves:
            return None
        filename = "__cache__/" + inspect.stack()[1][1] + "_name"
        if os.path.isfile(filename):
            with open(filename,'rb') as f:
                return pickle.load(f)
        else:
            return None

