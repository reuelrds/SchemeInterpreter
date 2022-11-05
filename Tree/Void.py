from Tree import Node


class Void(Node):
    """A Node which implements print method to print nothing"""

    _instance = None

    def __new__(cls, *args, **kwargs):

        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance

    def print(self, n, p=False):
        pass

    # This method is just for testing pruposes so that this class is compatible
    # with the reference binary files
    #
    # TODO: Remove this method once the interpreter is implementated
    @staticmethod
    def getInstance():

        if not Void._instance:
            Void()

        return Void._instance
