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
        
    # This method is just for testing pruposes so that this class is compatible
    # with the reference binary files
    #
    # TODO: Remove this method once the interpreter is implementated
    @staticmethod
    def getInstance():

        if not Unspecific._instance:
            Unspecific()

        return Unspecific._instance

