# If -- Parse tree node strategy for printing the special form if

from Tree import BoolLit
from Tree import Nil
from Tree import Unspecific
from Print import Printer
from Special import Special


class If(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printIf(t, n, p)

    def eval(self, exp, env):

        exp_length = Special.util.length(exp)

        if exp_length < 3 or exp_length > 4:
            self._error('invalid expression')
            return Nil.getInstance()

        else:

            test = exp.getCdr().getCar()
            consequent = exp.getCdr().getCdr().getCar()

            if test.eval(env) == BoolLit.getInstance(True):
                return consequent.eval(env)

            else:
                if exp_length == 3:
                    # There is no else clause
                    return Unspecific.getInstance()

                elif exp_length == 4:
                    alternate = exp.getCdr().getCdr().getCdr().getCar()
                    return alternate.eval(env)
