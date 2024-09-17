from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for c in operations:
            if c == "C":
                stack.pop()
                continue
            if c == "+":
                stack.append(int(stack[-1]) + int(stack[-2]))
                continue
            if c == "D":
                stack.append(stack[-1] * 2)
                continue
            stack.append(int(c))
        return sum(stack)


if __name__ == '__main__':
    ops = ["5", "2", "C", "D", "+"]
    s = Solution()
    a = s.calPoints(ops)
    print(a)

    ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    a = s.calPoints(ops)
    print(a)

    ops = ["1"]
    a = s.calPoints(ops)
    print(a)
