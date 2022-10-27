import sys
from Tree import Node


class Unspecific(Node):
    """A Node which implements print method to print #{Unspecific}"""

    _instance = None

    def __new__(cls, *args, **kwargs):

        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance

    def print(self, n, p=False):
        sys.stdout.write(r"#{Unspecific}")
