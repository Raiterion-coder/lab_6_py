import math
import sys
from typing import Union


class Function:
    def evaluate(self, x: float) -> float:
        raise NotImplementedError("Метод evaluate должен быть переопределен в производных классах")


class X(Function):
    def evaluate(self, x: float) -> float:
        return x


class SqrtFun(Function):
    def evaluate(self, x: float) -> float:
        return math.sqrt(x)


class Constant(Function):
    def __init__(self, value: float):
        self.value = value

    def evaluate(self, x: float) -> float:
        return self.value


class BinaryOperation(Function):
    def __init__(self, left: Function, right: Function, op: str):
        self.left = left
        self.right = right
        self.op = op

    def evaluate(self, x: float) -> float:
        left_val = self.left.evaluate(x)
        right_val = self.right.evaluate(x)
        if self.op == '+':
            return left_val + right_val
        elif self.op == '-':
            return left_val - right_val
        elif self.op == '*':
            return left_val * right_val
        elif self.op == '/':
            return left_val / right_val
        else:
            raise ValueError(f"Неизвестный оператор: {self.op}")


def parse_expression(expr: str, functions: dict[str, Function]) -> Function:
    tokens = expr.split()
    output = []
    stack = []

    for token in tokens:
        if token in functions or token.replace('.', '').replace('-', '').isdigit():
            output.append(token)
        elif token in '+-*/':
            while stack and stack[-1] in '+-*/':
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Удаляем '('

    while stack:
        output.append(stack.pop())

    func_stack = []
    for token in output:
        if token in functions:
            func_stack.append(functions[token])
        elif token.replace('.', '').replace('-', '').isdigit():
            func_stack.append(Constant(float(token)))
        elif token in '+-*/':
            if len(func_stack) < 2:
                raise ValueError(f"Недостаточно операндов для оператора {token}")
            right = func_stack.pop()
            left = func_stack.pop()
            func_stack.append(BinaryOperation(left, right, token))

    if len(func_stack) != 1:
        raise ValueError(f"Неверное выражение: {expr}")

    return func_stack[0]


def main():
    functions = {
        'x': X(),
        'sqrt_fun': SqrtFun()
    }

    n = int(sys.stdin.readline())
    for _ in range(n):
        line = sys.stdin.readline().strip()
        if not line:
            continue

        parts = line.split()
        if parts[0] == 'define':
            func_name = parts[1]
            func_expr = ' '.join(parts[2:])
            functions[func_name] = parse_expression(func_expr, functions)
        elif parts[0] == 'calculate':
            func_name = parts[1]
            points = list(map(float, parts[2:]))
            func = functions[func_name]
            results = [func.evaluate(x) for x in points]

            formatted = []
            for num in results:
                if num == int(num):
                    formatted.append(str(int(num)))
                else:
                    s = "{0:.15g}".format(num)
                    if '.' in s:
                        s = s.rstrip('0').rstrip('.')
                    formatted.append(s)
            print(' '.join(formatted))


if __name__ == "__main__":
    main()
