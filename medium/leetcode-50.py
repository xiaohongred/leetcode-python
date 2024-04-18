class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1.0 / x
            n = -1 * n

        res = 1
        for _ in range(n):
            res *= x
        return res

    def myPowV2(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        def pow(x, n):
            newN = n // 2
            remain = n % 2
            if newN > 20:
                res = pow(x, newN)
                if remain == 0:
                    return res * res
                else:
                    return res * res * x
            res = 1
            for _ in range(n):
                res *= x
            return res

        allRes = pow(x, abs(n))
        return allRes if n >= 0 else 1 / allRes


if __name__ == '__main__':
    x = 0.00001
    n = 2147483647
    s = Solution()
    a = s.myPowV2(x, n)
    print(a)
