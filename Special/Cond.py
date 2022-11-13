# Cond -- Parse tree node strategy for printing the special form cond

from Tree import BoolLit
from Tree import Nil
from Tree import Unspecific
from Print import Printer
from Special import Special


class Cond(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printCond(t, n, p)

    def _eval_expression(self, expression, env, predicate=None):

        if expression.getCar().isSymbol() and expression.getCar().getName() == "=>":
            expression = expression.getCdr()

            expression_value = expression.getCar().eval(env)

            if expression_value.isProcedure() and expression_value.parameter_count() == 1:
                return expression_value.apply(predicate.eval(env))
            else:
                self._error("Return Value is not a procedure")
                return Nil.getInstance()

        else:

            expression_length = Special.util.length(expression)

            if expression_length > 1:
                return Special.util.begin(expression, env)
            else:
                return expression.getCar().eval(env)

    def eval(self, exp, env):

        clause_count = Special.util.length(exp) - 1

        expressions = exp.getCdr()

        if clause_count < 1:
            self._error("Invalid Cond Expression")
            return Nil.getInstance()

        for _ in range(clause_count - 1):

            predicate = expressions.getCar().getCar()
            expression = expressions.getCar().getCdr()

            if predicate.eval(env) == BoolLit.getInstance(True):

                return self._eval_expression(expression, env, predicate)
            else:
                expressions = expressions.getCdr()

        else:

            predicate = expressions.getCar().getCar()
            expression = expressions.getCar().getCdr()

            if predicate.isSymbol() and predicate.getName() == "else":

                return self._eval_expression(expression, env)

            elif predicate.eval(env) == BoolLit.getInstance(True):

                return self._eval_expression(expression, env, predicate)

            else:
                return Unspecific.getInstance()
