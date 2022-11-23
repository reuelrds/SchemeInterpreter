# Closure -- the data structure for function closures

# Class Closure is used to represent the value of lambda expressions.
# It consists of the lambda expression itself, together with the
# environment in which the lambda expression was evaluated.

# The method apply() takes the environment out of the closure,
# adds a new frame for the function call, defines bindings for the
# parameters with the argument values in the new frame, and evaluates
# the function body.

import sys
from Tree import Node
from Tree import StrLit
from Tree import Environment
from Tree import Void


class Closure(Node):
    util = None

    @classmethod
    def setUtil(cls, u):
        cls.util = u

    def __init__(self, f, e):
        self.fun = f                    # a lambda expression
        self.env = e                    # the environment in which
        # the function was defined

    def getFun(self):
        return self.fun

    def getEnv(self):
        return self.env

    def isProcedure(self):
        return True

    def parameter_count(self):
        return Closure.util.length(self.fun.getCdr().getCar())

    def print(self, n, p=False):
        for _ in range(n):
            sys.stdout.write(' ')
        sys.stdout.write("#{Procedure")
        if self.fun != None:
            self.fun.print(abs(n) + 4)
        for _ in range(abs(n)):
            sys.stdout.write(' ')
        sys.stdout.write(" }\n")
        sys.stdout.flush()

    # TODO: The method apply() should be defined in class Node
    # to report an error.  It should be overridden only in classes
    # BuiltIn and Closure.
    def apply(self, args):
        varList = self.fun.getCdr().getCar()
        body = self.fun.getCdr().getCdr()
        newEnv = Environment(self.env)
        n = Closure.util.length(varList)

        # if varList.isNull() and args.isNull():
        #     pass

        # elif Closure.util.length(args) != n:
        #     self._error("number of arguments don't match")

        # elif varList.isSymbol():
        #     newEnv.define(varList, args)

        # i = 1

        # while i <= n:
        #     var = varList.getCar()
        #     val = args.getCar()
        #     newEnv.define(var, val)

        #     varList = varList.getCdr()
        #     i+=1

        while not (varList.isNull() and args.isNull()):


            if varList.isSymbol():
                newEnv.define(varList, args)

            elif varList.isPair() and args.isPair():
                val = args.getCar()
                var = varList.getCar()

                newEnv.define(var, val)

            if varList.isPair() and args.isPair():
                varList = varList.getCdr()
                args = args.getCdr()
            else:
                break

        return Closure.util.begin(body, newEnv)

    def eval(self, env):
        self._error("Environment.eval not yet implemented")
        return Void()
