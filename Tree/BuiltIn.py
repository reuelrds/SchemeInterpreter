# BuiltIn -- the data structure for built-in functions

# Class BuiltIn is used for representing the value of built-in functions
# such as +.  Populate the initial environment with
# (name, BuiltIn(name)) pairs.

# The object-oriented style for implementing built-in functions would be
# to include the Python methods for implementing a Scheme built-in in the
# BuiltIn object.  This could be done by writing one subclass of class
# BuiltIn for each built-in function and implementing the method apply
# appropriately.  This requires a large number of classes, though.
# Another alternative is to program BuiltIn.apply() in a functional
# style by writing a large if-then-else chain that tests the name of
# the function symbol.

import contextlib
import io
import re
import sys

from Parse import *
from Tree import Node
from Tree import BoolLit
from Tree import IntLit
from Tree import StrLit
from Tree import Ident
from Tree import Nil
from Tree import Cons
from Tree import TreeBuilder

from Tree import Unspecific
from Tree import Void

# TODO: Update Nil and BoolLit classes to use __new__


class BuiltIn(Node):
    env = None
    util = None

    @classmethod
    def setEnv(cls, e):
        cls.env = e

    @classmethod
    def setUtil(cls, u):
        cls.util = u

    def __init__(self, s):
        self.symbol = s                 # the Ident for the built-in function
        self._symbol_name = self.symbol.getName()

    def getSymbol(self):
        return self.symbol

    def isProcedure(self):
        return True

    def print(self, n, p=False):
        for _ in range(n):
            sys.stdout.write(' ')
        sys.stdout.write("#{Built-In Procedure ")
        if self.symbol != None:
            self.symbol.print(-abs(n) - 1)
        sys.stdout.write('}')
        if n >= 0:
            sys.stdout.write('\n')
            sys.stdout.flush()

    def eval(self, env):
        self._error("BuiltIn.eval not yet implemented")
        return Void()

    # TODO: The method apply() should be defined in class Node
    # to report an error.  It should be overridden only in classes
    # BuiltIn and Closure.
    def apply(self, args):

        args_count = BuiltIn.util.length(args)

        if args_count == 0:
            return self._apply()

        elif args_count == 1:
            return self._apply_unary(args)

        elif args_count == 2:
            return self._apply_binary(args)

        else:
            self._error("Unsupported Number of arguments")
            return Void()

        # The easiest way to implement BuiltIn.apply is as an
        # if-then-else chain testing for the different names of
        # the built-in functions.  E.g., here's how load could
        # be implemented:

        # if name == "load":
        #     if not arg1.isString():
        #         self._error("wrong type of argument")
        #         return Nil.getInstance()
        #     filename = arg1.getStrVal()
        #     try:
        #         scanner = Scanner(open(filename))
        #         builder = TreeBuilder()
        #         parser = Parser(scanner, builder)

        #         root = parser.parseExp()
        #         while root != None:
        #             root.eval(BuiltIn.env)
        #             root = parser.parseExp()
        #     except IOError:
        #         self._error("could not find file " + filename)
        #     return Nil.getInstance()  # or Unspecific.getInstance()

    def _apply(self):

        if self._symbol_name == "newline":
            sys.stdout.write("\n")
            return Unspecific.getInstance()

        elif self._symbol_name == "read":

            scanner = Scanner(sys.stdin)
            builder = TreeBuilder()
            parser = Parser(scanner, builder)

            root = parser.parseExp()

            if root is not None:
                return root

            else:
                # TODO: Do we need to Flush to stdout
                # after writing a newline character?

                sys.stdout.write("#{End-of-file}")
                sys.stdout.write("\n")
                return Void()

        elif self._symbol_name == "interaction-environment":
            return BuiltIn.env

        else:
            self._error(
                f"Apply method is not defined for `{self._symbol_name}`")
            return Void()

    def _apply_unary(self, args):

        arg1 = args.getCar()

        if self._symbol_name[-1] == "?":
            return self._check_arg_node_type(arg1)

        elif self._symbol_name == "car":
            return arg1.getCar()

        elif self._symbol_name == "cdr":
            return arg1.getCdr()

        elif self._symbol_name == "write":

            # TODO: Check if the indentation is correct

            arg1.print(0)
            return Unspecific.getInstance()

        elif self._symbol_name == "display":

            # This with block captures the buffer before it is
            # written to stdout, which allows us to replace the
            # double qoute characters around a string with nothing
            #
            # Credits: https://stackoverflow.com/a/22434594

            # TODO: Should we flush the stdout buffer before calling print?

            with io.StringIO() as buf, contextlib.redirect_stdout(buf):

                # TODO: Check if the indentation is correct
                arg1.print(0)
                output = buf.getvalue()

            output = re.sub(r"\"", r"", output.strip())
            sys.stdout.write(output)
            return Unspecific.getInstance()

        # Copied Verbatim from the Skeleton Code
        elif self._symbol_name == "load":

            if not arg1.isString():
                self._error("wrong type of argument")
                return Nil.getInstance()
            filename = arg1.getStrVal()

            try:
                scanner = Scanner(open(filename))
                builder = TreeBuilder()
                parser = Parser(scanner, builder)

                root = parser.parseExp()
                while root != None:
                    root.eval(BuiltIn.env)
                    root = parser.parseExp()
            except IOError:
                self._error("could not find file " + filename)
            return Void()  # or Unspecific.getInstance()

        else:
            self._error(
                f"Apply method is not defined for `{self._symbol_name}`")
            return Void()

    def _apply_binary(self, args):

        arg1 = args.getCar()
        arg2 = args.getCdr().getCar()

        if self._symbol_name == "cons":

            # TODO: Check if we can just return args instead
            #       of constructing a new object
            return Cons(arg1, arg2)

        elif self._symbol_name == "apply":
            return arg1.apply(arg2)

        elif self._symbol_name == "eval":

            if arg2.isEnvironment():
                return arg1.eval(arg2)
            else:
                self._error(f"Invalid Environment - `{arg2}`")
                return Void()

        elif self._symbol_name[0] == "b":

            if not arg1.isNumber():

                self._error(f"`{arg1}` is not a Number")
                return Void()

            if not arg2.isNumber():

                self._error(f"`{arg2}` is not a Number")
                return Void()

            return self._binary_arithmetic(arg1.intVal, arg2.intVal)

        elif self._symbol_name == "set-car!":
            arg1.setCar(arg2)
            return Unspecific.getInstance()

        elif self._symbol_name == "set-cdr!":
            arg1.setCdr(arg2)
            return Unspecific.getInstance()

        # TODO: Check if eq? implementation is correct.
        #       Should we just check if both the objects are same? Or
        #       Sdould we check if the both the objects have same
        #       structure (i.e. Nodes with same identifiers and literals)?
        elif self._symbol_name == "eq?":
            return BoolLit.getInstance(arg1 == arg2)

        else:
            self._error(
                f"Apply method is not defined for `{self._symbol_name}`")
            return Void()

    def _binary_arithmetic(self, arg1, arg2):

        if self._symbol_name == "b+":
            return IntLit(arg1 + arg2)

        elif self._symbol_name == "b-":
            return IntLit(arg1 - arg2)

        elif self._symbol_name == "b*":
            return IntLit(arg1 * arg2)

        elif self._symbol_name == "b/":
            return IntLit(arg1 / arg2)

        elif self._symbol_name == "b=":
            return BoolLit.getInstance(arg1 == arg2)

        elif self._symbol_name == "b<":
            return BoolLit.getInstance(arg1 < arg2)

        else:
            self._error(
                f"Apply method is not defined for `{self._symbol_name}`")
            return Void()

    def _check_arg_node_type(self, arg1):

        if self._symbol_name == "number?":
            return BoolLit.getInstance(arg1.isNumber())

        elif self._symbol_name == "symbol?":
            return BoolLit.getInstance(arg1.isSymbol())

        elif self._symbol_name == "null?":
            return BoolLit.getInstance(arg1.isNull())

        elif self._symbol_name == "pair?":
            return BoolLit.getInstance(arg1.isPair())

        elif self._symbol_name == "procedure?":
            return BoolLit.getInstance(arg1.isProcedure())

        else:
            self._error(
                f"Apply method is not defined for `{self._symbol_name}`")
            return Void()
