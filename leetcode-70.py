class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        one, two = 1, 2
        for i in range(2, n):  # 这里只关注循环次数， 这个题和斐波拉契数列一样
            temp = two
            two = one + two
            one = temp

        return two

    def climbStairsV2(self, n: int) -> int:
        cache = {}

        def dp(n: int):
            if n in cache:
                return cache[n]

            if n == 1 or n == 2 or n == 0:
                cache[n] = n
                return n
            cache[n] = dp(n - 1) + dp(n - 2)
            return cache[n]

        return dp(n)


if __name__ == '__main__':
    n = 3
    s = Solution()
    a = s.climbStairs(n)
    print(a)

    a = s.climbStairsV2(n)
    print(a)
