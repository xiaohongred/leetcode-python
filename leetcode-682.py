from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                s = stack[-1] + stack[-2]
                stack.append(s)
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)


if __name__ == '__main__':
    ops = ["5", "2", "C", "D", "+"]
    s = Solution()
    a = s.calPoints(ops)
    print(a)
