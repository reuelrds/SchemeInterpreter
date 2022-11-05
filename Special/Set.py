# Set -- Parse tree node strategy for printing the special form set!

from Tree import Nil
from Tree import Unspecific
from Print import Printer
from Special import Special

class Set(Special):
    def __init__(self):
        pass
    
    def print(self, t, n, p):
        Printer.printSet(t, n, p)

    def eval(self, exp, env):
        if Special.util.length(exp) != 3:
            self._error("expression not valid")
            return Nil.getInstance()
        
        var = exp.getCdr().getCar()
        val = exp.getCdr().getCdr().getCar()
        
        env.assign(var, val.eval(env))
        return Unspecific.getInstance()