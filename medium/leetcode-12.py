class Solution:
    def intToRoman(self, num: int) -> str:
        symList = [
            ["I", 1], ["IV", 4], ["V", 5], ["IX", 9],
            ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
            ["C", 100], ["CD", 400], ["D", 500], ["CM", 900],
            ["M", 1000]
        ]
        res = ""
        for sym, val in reversed(symList):
            if num // val:
                count = num // val
                res += (sym * count)
            num = num % val
        return res


if __name__ == '__main__':
    num = 3
    s = Solution()
    a = s.intToRoman(num)
    print(a)
    num = 4
    a = s.intToRoman(num)
    print(a)
    num = 9
    a = s.intToRoman(num)
    print(a)
    num = 58
    a = s.intToRoman(num)
    print(a)
    num = 1994
    a = s.intToRoman(num)
    print(a)
