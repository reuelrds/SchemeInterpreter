# Let -- Parse tree node strategy for printing the special form let

from Tree import Nil
from Tree import Environment
from Print import Printer
from Special import Special

class Let(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printLet(t, n, p)

    def eval(self, exp, env):
        if Special.util.length(exp) < 3:
            self._error("expression not valid")
            return Nil.getInstance()

        varList = exp.getCdr().getCar()
        n = Special.util.length(varList)

        if n < 1:
            self._error("expression not valid")
            return Nil.getInstance()

        i = 1
        newEnv = Environment(env)

        while i <= n:
            varPair = varList.getCar()
            if Special.util.length(varPair) != 2:
                self._error("expression not valid")
                return Nil.getInstance()

            var = varPair.getCar()
            val = varPair.getCdr().getCar().eval(env)
            newEnv.define(var, val)

            varList = varList.getCdr()
            i+=1

        return exp.getCdr().getCdr().getCar().eval(newEnv)