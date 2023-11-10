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


if __name__ == '__main__':
    n = 3
    s = Solution()
    a = s.climbStairs(n)
    print(a)
