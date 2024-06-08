class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        mStack = []
        for c in num:
            while k > 0 and mStack and mStack[-1] > c:
                k -= 1
                mStack.pop()
            mStack.append(c)

        mStack = mStack[:(len(mStack) - k)]
        res = "".join(mStack)
        while len(res) > 0 and res[0] == "0":
            res = res[1:]
        return res if res else "0"


if __name__ == '__main__':
    num = "1432219"
    k = 3

    s = Solution()
    a = s.removeKdigits(num, k)
    print(a)
