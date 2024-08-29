class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # dp[j][c] = num of strs of len=j where last char is c
        dp = [[], [1, 1, 1, 1, 1]]  # 第0行，都为空，第一行，代表字符串长度为1，以字母 a,e,i,o,u 结尾的字符串的个数

        a, e, i, o, u = 0, 1, 2, 3, 4
        mod = 10 ** 9 + 7
        for j in range(2, n + 1):
            dp.append([0, 0, 0, 0, 0])
            # 看哪些字母之后可以跟 a
            dp[j][a] = (dp[j - 1][e] +  # e 后面可以跟a        dp[j - 1][e]代表长度为 j-1 结尾为字符e 的字符串的个数
                        dp[j - 1][i] +  # i 后面可以跟a, 因为 i后面只不能跟i
                        dp[j - 1][u]  # u 后面只能跟a
                        ) % mod
            # 哪些字母之后可以跟 e
            dp[j][e] = (dp[j - 1][a] +  # a 后面只能跟e
                        dp[j - 1][i]  # i 后面可以跟e, 因为 i后面只不能跟i
                        ) % mod
            # 哪些字母之后可以跟 i
            dp[j][i] = (dp[j - 1][e] +  # e 后面可以跟i
                        dp[j - 1][o]  # o 后面可以跟i, 因为 o 后面可以跟着i 或者 u
                        ) % mod

            # 看 哪些字符之后可以跟 o
            dp[j][o] = (
                           dp[j - 1][i]  # 看 哪些字符之后可以跟 o, 发现 只有 i 后面可以跟o
                       ) % mod

            # 看哪些字符之后可以跟u
            dp[j][u] = (dp[j - 1][i] +  # 看哪些字符之后可以跟u,发现 i, u 字母之后可以跟u
                        dp[j - 1][o]
                        ) % mod
        return sum(dp[n]) % mod


if __name__ == '__main__':
    n = 1
    s = Solution()
    a = s.countVowelPermutation(n)
    print(a)

    n = 2
    a = s.countVowelPermutation(n)
    print(a)

    n = 5
    a = s.countVowelPermutation(n)
    print(a)
