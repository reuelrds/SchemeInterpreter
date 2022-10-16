# Parser -- the parser for the Scheme printer and interpreter
#
# Defines
#
#   class Parser
#
# Parses the language
#
#   exp  ->  ( rest
#         |  #f
#         |  #t
#         |  ' exp
#         |  integer_constant
#         |  string_constant
#         |  identifier
#    rest -> )
#         |  exp+ [. exp] )
#
#
# Converted rest into BNF form
#
#    rest -> )
#         |  exp rest
#         |  exp . exp )
#
#
# Left Factored rest expression
#
#    rest -> )
#         |  exp rest'
#
#    rest'-> . exp )
#         |  rest
#
#
#
# and builds a parse tree.  Lists of the form (rest) are further
# `parsed' into regular lists and special forms in the constructor
# for the parse tree node class Cons.  See Cons.parseList() for
# more information.
#
# The parser is implemented as an LL(0) recursive descent parser.
# I.e., parseExp() expects that the first token of an exp has not
# been read yet.  If parseRest() reads the first token of an exp
# before calling parseExp(), that token must be put back so that
# it can be re-read by parseExp() or an alternative version of
# parseExp() must be called.
#
# If EOF is reached (i.e., if the scanner returns None instead of a token),
# the parser returns None instead of a tree.  In case of a parse error, the
# parser discards the offending token (which probably was a DOT
# or an RPAREN) and attempts to continue parsing with the next token.

import sys

import Tree

from Tokens import TokenType
from Tokens import Token


class Parser:
    def __init__(self, s):
        self.scanner = s

    def parseExp(self):
        return self.__parseExp(self.scanner.getNextToken())

    def __parseExp(self, token: Token):

        # End of input
        if token is None:
            return

        elif token.getType() == TokenType.LPAREN:
            return self.parseRest()

        elif token.getType() == TokenType.TRUE:
            return Tree.BoolLit.getInstance(True)

        elif token.getType() == TokenType.FALSE:
            return Tree.BoolLit.getInstance(False)

        elif token.getType() == TokenType.QUOTE:

            # Parses '(a) as (quote (a))
            return Tree.Cons(Tree.Ident("quote"), Tree.Cons(self.parseExp(), Tree.Nil.getInstance()))

        elif token.getType() == TokenType.INT:
            return Tree.IntLit(token.getIntVal())

        elif token.getType() == TokenType.STR:
            return Tree.StrLit(token.getStrVal())

        elif token.getType() == TokenType.IDENT:
            return Tree.Ident(token.getName())

        # Sanity Check.
        # The . should only be recognized by the rest' rule
        # If the token is a . then it means that the input expression is not valid
        elif token.getType() == TokenType.DOT:
            self.__error("Illegal DOT in the expression")

        # Sanity Check.
        # The ) should only be recognized by the rest rule
        elif token.getType() == TokenType.RPAREN:
            self.__error("Illegal Right Parenthesis in the expression")

        # To handle the case when the parser can't recognize the input.
        # i.e. either there's an error in the parser or the input expression is not valid
        else:
            self.__error("Error in parsing token from the input")

    def parseRest(self):
        return self.__parseRest(self.scanner.getNextToken())

    def __parseRest(self, token: Token):

        if token is None:
            return

        elif token.getType() == TokenType.RPAREN:
            return Tree.Nil.getInstance()

        else:
            car = self.__parseExp(token)
            cdr = self.parseRestPrime()

            if car is None or cdr is None:
                self.__error("Error in parsing the input")
                return

            else:
                return Tree.Cons(car, cdr)

    def parseRestPrime(self):
        token = self.scanner.getNextToken()

        if token is None:
            return

        elif token.getType() == TokenType.DOT:

            # As the token is a DOT token, the return value of the parseExp
            # in the previous call to parseExp from __parseRest will go
            # in the car of the CONS node (Line 144) and the return value of
            # the following call to parseExp will go to the cdr of the CONS node
            # if the next token is a RPAREN.
            cdr = self.parseExp()
            token = self.scanner.getNextToken()

            if token is None:
                return

            elif token.getType() == TokenType.RPAREN:
                return cdr

            else:
                self.__error(f"Expected a RPAREN after an expression following DOT. Got: {token}")
                return

        else:
            return self.__parseRest(token)

    def __error(self, msg):
        sys.stderr.write("Parse error: " + msg + "\n")
