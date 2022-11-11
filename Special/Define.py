# Define -- Parse tree node strategy for printing the special form define

from Tree import Ident
from Tree import Nil
from Tree import Cons
#from Tree import Void
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
            return Nil.getInstance()

        declaration = exp.getCdr().getCar()
        body = exp.getCdr().getCdr().getCar()

        # Variable Definition
        if not declaration.isPair():

            env.define(declaration, body.eval(env))
            return Nil.getInstance()

        # Function Definition
        elif declaration.isPair():

            variable = declaration.getCar()

            if declaration.getCdr().isPair():
                formal = declaration.getCdr().getCar()
            else:
                formal = declaration.getCdr()

            lambd = Cons(
                Ident("lambda"),
                Cons(
                    Cons(formal, Nil.getInstance()),
                    Cons(body, Nil.getInstance())
                )
            )
            env.define(variable, lambd.eval(env))

            return Nil.getInstance()
