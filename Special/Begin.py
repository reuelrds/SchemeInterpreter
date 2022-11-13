# Begin -- Parse tree node strategy for printing the special form begin

from Tree import Nil
from Print import Printer
from Special import Special


class Begin(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printBegin(t, n, p)

    def eval(self, exp, env):

        exp_length = Special.util.length(exp)

        if exp_length < 2:
            self._error('invalid expression')
            return Nil.getInstance()
        
        return Special.util.begin(exp.getCdr(), env)
