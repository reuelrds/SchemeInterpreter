# Define -- Parse tree node strategy for printing the special form define

from Tree import Ident
from Tree import Nil
from Tree import Cons
from Tree import Void
from Print import Printer
from Special import Special


class Define(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printDefine(t, n, p)

    def eval(self, exp, env):

        exp_length = Special.util.length(exp)

        if exp_length < 3:
            self._error('invalid expression')
            return Void.getInstance()

        declaration = exp.getCdr().getCar()
        body = exp.getCdr().getCdr()

        # Variable Definition
        if not declaration.isPair():

            env.define(declaration, body.getCar().eval(env))
            return Void.getInstance()

        # Function Definition
        elif declaration.isPair():

            variable = declaration.getCar()

            formal = declaration.getCdr()

            lambd = Cons(
                Ident("lambda"),
                Cons(formal, body)
            )
            # lambd.print(0)
            env.define(variable, lambd.eval(env))

            return Void.getInstance()
        
    