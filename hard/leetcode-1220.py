class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # dp[j][c] = num of strs of len=j
        # where last char is c:
        dp = [[], [1, 1, 1, 1, 1]]  # dp[j] 的定义是 j个数，按照题目规则有多少种组成方式

        a, e, i, o, u = 0, 1, 2, 3, 4
        mod = 10 ** 9 + 7
        for j in range(2, n + 1):
            dp.append([0, 0, 0, 0, 0])
            dp[j][a] = (dp[j - 1][e] +  # e 后面可以跟着 a
                        dp[j - 1][i] +  # i 后面可以跟着a
                        dp[j - 1][u]  # u 后面可以跟着a
                        ) % mod
            dp[j][e] = (dp[j - 1][a] +  # a 后面可以跟 e
                        dp[j - 1][i]  # i 后面可以跟着 e
                        ) % mod

            dp[j][i] = (dp[j - 1][e] +  # e 后面可以跟着 i
                        dp[j - 1][o]  # o 后面可以跟着 i
                        ) % mod

            dp[j][o] = (dp[j - 1][i]) % mod
            dp[j][u] = (dp[j - 1][i] + dp[j - 1][o]) % mod

        return sum(dp[n]) % mod


if __name__ == '__main__':
    s = Solution()

    n = 1
    a = s.countVowelPermutation(n)
    print(a)

    n = 2
    a = s.countVowelPermutation(n)
    print(a)

    n = 5
    a = s.countVowelPermutation(n)
    print(a)

    n = 100
    a = s.countVowelPermutation(n)
    print(a)
