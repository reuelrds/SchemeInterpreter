# Regular -- Parse tree node strategy for printing regular lists

from Tree import Void
from Print import Printer
from Special import Special

class Regular(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printRegular(t, n, p)

    def eval(self, exp, env):
        if Special.util.length(exp) < 1:
            self._error("expression not valid")
            return Void.getInstance()
        
        fcn = exp.getCar().eval(env)
        arguments = Special.util.mapeval(exp.getCdr(), env)

        return fcn.apply(arguments)
