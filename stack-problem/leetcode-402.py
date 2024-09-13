import sys


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []  # we want monotonic stack
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)

        while k > 0 and stack:
            stack.pop()
            k -= 1
        if len(stack) == 0:
            return "0"
        i = 0
        while i < len(stack) and stack[i] == "0":
            i += 1

        stack = stack[i:]
        res = "".join(stack)
        if res == "":
            res = "0"
        return res

    def removeKdigitsV2(self, num: str, k: int) -> str:
        stack = []
        sys.set_int_max_str_digits(1000000000)
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)
        stack = stack[:len(stack) - k]
        res = "".join(stack)
        return str(int(res)) if res else "0"


if __name__ == '__main__':
    num = "1432219"
    k = 3
    s = Solution()
    a = s.removeKdigits(num, k)
    print(a)

    num = "10200"
    k = 1
    a = s.removeKdigits(num, k)
    print(a)

    num = "10"
    k = 2
    a = s.removeKdigits(num, k)
    print(a)

    num = "9"
    k = 1
    a = s.removeKdigits(num, k)
    print(a)
