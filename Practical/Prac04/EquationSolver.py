# Cite from DSA Prac03

from DSAStack import Stack
from DSAQueue import Queue

class EquationSolver():

    def __init__(self):
        self.queueInfix = Queue()
        self.queuePostfix = Queue()
        self.stackOperand = Stack()
        self.stackOperator = Stack()

    def _isOperator(self, term):
        return term == '+' or term == '-' or term == '*' or term == '/'

    def _parseTerm(self, term):
        term = term.strip()
        try:
            operand = float(term)
            return operand
        except ValueError:
            if self._isOperator(term):
                return term[0]
            elif term == '(' or term == ')':
                return term[0]
            else:
                raise ValueError(f"parse term fail: {term}")

    def _parseInfixToPostfix(self, equation):
        rep = ["(", " ( ", ")", " ) ", "+", " + ", "-", " - ", "*", " * ", "/", " / "]
        for i in range(0, len(rep), 2):
            equation = equation.replace(rep[i], rep[i + 1])
        infixTerms = equation.split()
        postfix = ""
        for infixTerm in infixTerms:
            self.queueInfix.enqueue(self._parseTerm(infixTerm))
        print(f"Infix: {self.queueInfix}")
        while self.queueInfix.getCount() != 0:
            term = self.queueInfix.dequeue()
            if term == '(':
                self.stackOperator.push(term)
            elif term == ')':
                while self.stackOperator.top() != '(':
                    self.queuePostfix.enqueue(self.stackOperator.pop())
                self.stackOperator.pop()
            elif self._isOperator(term):
                while (not self.stackOperator.isEmpty()) \
                        and self.stackOperator.top() != '(' \
                        and self._precedenceOf(self.stackOperator.top()) \
                                >= self._precedenceOf(term):
                    self.queuePostfix.enqueue(self.stackOperator.pop())
                self.stackOperator.push(term)
            else:
                self.queuePostfix.enqueue(term)
        while (not self.stackOperator.isEmpty()):
            self.queuePostfix.enqueue(self.stackOperator.pop())
        print(f"Postfix: {self.queuePostfix}")

    def _evaluatePostfix(self, postfixQueue):
        while postfixQueue.getCount() != 0:
            term = postfixQueue.dequeue()
            if self._isOperator(term):
                op2 = self.stackOperand.pop()
                op1 = self.stackOperand.pop()
                ans = self._executeOperation(term, op1, op2)
                self.stackOperand.push(ans)
            else:
                self.stackOperand.push(term)
        if self.stackOperand.getCount() != 1:
            raise ValueError("Input infix ERROR!")
        print(f"Operand: {self.stackOperand}")
        return self.stackOperand.pop()

    def _precedenceOf(self, theOp):
        if theOp == '+' or theOp == '-':
            return 1
        elif theOp == '*' or theOp == '/':
            return 2
        else:
            raise ValueError(f"Unkonwn Operator: {theOp}")

    def _executeOperation(self, op, op1, op2):
        try:
            if op == '+':
                return op1 + op2
            elif op == '-':
                return op1 - op2
            elif op == '*':
                return op1 * op2
            elif op == '/':
                return op1 / op2
            else:
                raise ValueError(f"Unknown Operation: {op} {op1} {op2}")
        except TypeError:
            raise ValueError(f"Input infix ERROR! {op} {op1} {op2}")

    def solve(self, equation):
        self._parseInfixToPostfix(equation)
        return self._evaluatePostfix(self.queuePostfix)


def test():
    testSolver = EquationSolver()

    testEqu = "( 10.3 * (14 + 3.2)) / (5 + 2 - 4 * 3)"
    ans = testSolver.solve(testEqu)
    print(f"Equation={testEqu}")
    print(f"Answer={ans}")
    assert ans == -35.432

    testEqu = "(10.3*(14+3.2))/(5+2-4*3)"
    ans = testSolver.solve(testEqu)
    print(f"Equation={testEqu}")
    print(f"Answer={ans}")
    assert ans == -35.432

    testEqu = "1.3*(1+2)/(3-4*3)"
    ans = testSolver.solve(testEqu)
    print(f"Equation={testEqu}")
    print(f"Answer={ans}")
    assert ans == 3.9/-9

    while True:
        print()
        testEqu = input("Please input your EQUATION here: ")
        try:
            ans = testSolver.solve(testEqu)
            print(f"Equation={testEqu}")
            print(f"Answer={ans}")
        except ValueError as e:
            print("ERROR:", e)


if __name__ == "__main__":
    test()
