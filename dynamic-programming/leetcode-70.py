class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        arr = [0] * (n + 1)
        arr[1] = 1
        arr[2] = 2

        for i in range(3, n + 1):
            arr[i] = arr[i - 1] + arr[i - 2]
        return arr[n]


if __name__ == '__main__':
    n = 3
    s = Solution()
    a = s.climbStairs(n)
    print(a)

    n = 2
    a = s.climbStairs(n)
    print(a)

    n = 5
    a = s.climbStairs(n)
    print(a)
