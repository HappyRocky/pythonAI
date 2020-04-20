# -*- coding: utf-8 -*-

"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.
Note:
Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.

计算出逆波兰式的算术表达式的值。
有效的操作符有 +,-,*,/。每个操作数可能是一个整数或其他表达式。
备注：
两个整数的除法需要趋零截尾。
给定的 RPN 表达式总是有效的，即表达式总是可以计算出一个结果，并且没有零操作数的除法。

Example 1:
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

def evalRPN(tokens: list) -> int:
    """
    使用栈计算。
    """
    stack = []
    for token in tokens:
        try:
            stack.append(int(token))
        except:
            a1 = stack.pop()
            a2 = stack.pop()
            if token == '+':
                stack.append(a2 + a1)
            elif token == '-':
                stack.append(a2 - a1)
            elif token == '*':
                stack.append(a2 * a1)
            else:
                stack.append(int(a2 / a1))
    return stack[0]

if '__main__' == __name__:
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(evalRPN(tokens))