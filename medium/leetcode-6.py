class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = ""
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                res += s[i]
                if 0 < r < numRows - 1 \
                        and i + increment - 2 * r < len(s):
                    res += s[i + increment - 2 * r]
        return res


if __name__ == '__main__':
    s = Solution()
    testStr = "A"
    numRows = 1
    a = s.convert(testStr, numRows)
    print(a)

    testStr = "PAYPALISHIRING"
    numRows = 3
    a = s.convert(testStr, numRows)
    print(a)
