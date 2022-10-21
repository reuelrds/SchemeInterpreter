from Tree import Node

class None_(Node):
    """A Node which implements print method to print nothing"""

    _instance = None

    def __new__(cls, *args, **kwargs):

        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance

    def print(self, n, p=False):
        pass
