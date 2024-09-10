from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif c == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif c == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif c == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(c))
        return stack[0]


if __name__ == '__main__':
    s = Solution()
    tokens = ["2", "1", "+", "3", "*"]
    a = s.evalRPN(tokens)
    print(a)

    tokens = ["4", "13", "5", "/", "+"]
    a = s.evalRPN(tokens)
    print(a)

    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    a = s.evalRPN(tokens)
    print(a)
