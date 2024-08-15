class Solution:
    def minDays(self, n: int) -> int:
        cache = {0: 0, 1: 1}  # number of oranges -> mini day to eat

        def dfs(num):
            if num in cache:
                return cache[num]
            # if num == 0:
            #     return 0
            # if num == 1:
            #     return 1

            r1, r2, r3 = num, num, num

            if num % 2 == 0:
                r1 = 1 + dfs(num // 2)

            if num % 3 == 0:
                r2 = 1 + dfs(num // 3)

            r3 = 1 + dfs(num - 1)
            res = min(r1, r2, r3)
            cache[num] = res
            return res

        return int(dfs(n))

    def minDaysDP(self, n: int) -> int:
        dp = {0: 0, 1: 1}

        def dfs(n: int) -> int:
            if n in dp:
                return dp[n]
            typeDay1 = dfs(n // 2) + n % 2 + 1
            typeDay2 = dfs(n // 3) + n % 3 + 1
            dp[n] = min(typeDay1, typeDay2)
            return dp[n]

        a = dfs(n)
        return min(a, n)


if __name__ == '__main__':
    n = 10
    s = Solution()
    a = s.minDays(n)
    print(a)

    n = 10
    a = s.minDaysDP(n)
    print(a)
