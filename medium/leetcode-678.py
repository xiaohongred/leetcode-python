class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0  # number of left open parenthesis
        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:  # c == *
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:  # s = ))((
                return False
            if leftMin < 0:  # s = (*)(
                leftMin = 0
        return leftMin == 0


if __name__ == '__main__':
    s = "()"
    solu = Solution()
    a = solu.checkValidString(s)
    print(a)

    s = "(*)"
    a = solu.checkValidString(s)
    print(a)
    s = "(*))"
    a = solu.checkValidString(s)
    print(a)

    s = "(*))))*"
    a = solu.checkValidString(s)
    print(a)
