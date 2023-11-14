class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        primeList = [2, 3, 5]
        for pri in primeList:
            while n % pri == 0:
                n = n // pri

        if n == 1:
            return True

        if n in primeList:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    a = s.isUgly(14)
    b = s.isUgly(19)
    c = s.isUgly(6)
    d = s.isUgly(15)
    print(a, b, c, d)
