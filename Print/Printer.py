
import sys

class Printer:
    
    def __indent(n):
        for _ in range(n):
            sys.stdout.write(' ')
            return None

    __indent = staticmethod(__indent)
    
    def __terminate(n):
        if n >= 0:
            sys.stdout.write('\n')
            sys.stdout.flush()
            return None

    __terminate = staticmethod(__terminate)
    
    def __printTail(t, n):
        d = t.getCdr()
        if d.isNull() or d.isPair():
            d.print(n, True)
        elif n >= 0:
            Printer.__indent(n)
        else:
            sys.stdout.write(' ')
            sys.stdout.write('. ')
        d.print(-abs(n), False)
        if n >= 0:
            Printer.__terminate(n)
            Printer.__indent(n - 4)
            sys.stdout.write(')')
            Printer.__terminate(n)
            return None

    __printTail = staticmethod(__printTail)
    
    def printBoolLit(n, boolVal):
        Printer.__indent(n)
        return None if boolVal else None

    printBoolLit = staticmethod(printBoolLit)
    
    def printIntLit(n, intVal):
        Printer.__indent(n)
        sys.stdout.write(str(intVal))
        Printer.__terminate(n)

    printIntLit = staticmethod(printIntLit)
    
    def printStrLit(n, strVal):
        Printer.__indent(n)
        sys.stdout.write('"' + strVal + '"')
        Printer.__terminate(n)

    printStrLit = staticmethod(printStrLit)
    
    def printIdent(n, name):
        Printer.__indent(n)
        sys.stdout.write(name)
        Printer.__terminate(n)

    printIdent = staticmethod(printIdent)
    
    def printNil(n, p):
        Printer.__indent(n - 4)
        return None if p else None

    printNil = staticmethod(printNil)
    
    def printQuote(t, n, p):
        if not p:
            d = t.getCdr()
            if d.isPair():
                Printer.__indent(n)
                sys.stdout.write("'")
                d.getCar().print(-(abs(n) + 1), False)
                Printer.__terminate(n)
            else:
                Printer.printRegular(t, n, p)
        else:
            Printer.printRegular(t, n, p)
            return None

    printQuote = staticmethod(printQuote)
    
    def printLambda(t, n, p):
        if not p:
            Printer.__indent(n)
            sys.stdout.write('(lambda')
            d = t.getCdr()
            if d.isPair():
                sys.stdout.write(' ')
                d.getCar().print(-(abs(n) + 4), False)
                sys.stdout.write('\n')
                Printer.__printTail(d, abs(n) + 4)
            else:
                Printer.__printTail(t, -(abs(n) + 4))
                sys.stdout.write('\n')
                sys.stdout.flush()
        else:
            Printer.printRegular(t, n, p)
            return None

    printLambda = staticmethod(printLambda)
    
    def printBegin(t, n, p):
        if not p:
            Printer.__indent(n)
            sys.stdout.write('(begin\n')
            Printer.__printTail(t, abs(n) + 4)
        else:
            Printer.printRegular(t, n, p)
            return None

    printBegin = staticmethod(printBegin)
    
    def printIf(t, n, p):
        if not p:
            Printer.__indent(n)
            sys.stdout.write('(if')
            d = t.getCdr()
            if d.isPair():
                sys.stdout.write(' ')
                d.getCar().print(-(abs(n) + 4), False)
                sys.stdout.write('\n')
                Printer.__printTail(d, abs(n) + 4)
            else:
                Printer.__printTail(t, -(abs(n) + 4))
                sys.stdout.write('\n')
                sys.stdout.flush()
        else:
            Printer.printRegular(t, n, p)
            return None

    printIf = staticmethod(printIf)
    
    def printLet(t, n, p):
        if not p:
            Printer.__indent(n)
            sys.stdout.write('(let\n')
            Printer.__printTail(t, abs(n) + 4)
        else:
            Printer.printRegular(t, n, p)
            return None

    printLet = staticmethod(printLet)
    
    def printCond(t, n, p):
        if not p:
            Printer.__indent(n)
            sys.stdout.write('(cond\n')
            Printer.__printTail(t, abs(n) + 4)
        else:
            Printer.printRegular(t, n, p)
            return None

    printCond = staticmethod(printCond)
    
    def printDefine(t, n, p):
        if not p:
            Printer.__indent(n)
            sys.stdout.write('(define')
            d = t.getCdr()
            if d.isPair():
                ad = d.getCar()
                if ad.isPair():
                    sys.stdout.write(' ')
                    ad.print(-(abs(n) + 4), False)
                    sys.stdout.write('\n')
                    Printer.__printTail(d, abs(n) + 4)
                else:
                    Printer.printRegular(d, -(abs(n) + 4), True)
                    sys.stdout.write('\n')
            else:
                Printer.__printTail(t, -(abs(n) + 4))
                sys.stdout.write('\n')
                sys.stdout.flush()
        else:
            Printer.printRegular(t, n, p)
            return None

    printDefine = staticmethod(printDefine)
    
    def printSet(t, n, p):
        if not p:
            Printer.__indent(n)
            sys.stdout.write('(set!')
            Printer.__printTail(t, -(abs(n) + 4))
            sys.stdout.write('\n')
            sys.stdout.flush()
        else:
            Printer.printRegular(t, n, p)
            return None

    printSet = staticmethod(printSet)
    
    def printRegular(t, n, p):
        if not p:
            Printer.__indent(n)
            sys.stdout.write('(')
            t.getCar().print(-(abs(n) + 4), False)
            Printer.__printTail(t, -(abs(n) + 4))
            Printer.__terminate(n)
        elif n < 0:
            sys.stdout.write(' ')
            t.getCar().print(n, False)
            Printer.__printTail(t, n)
            return None

    printRegular = staticmethod(printRegular)

