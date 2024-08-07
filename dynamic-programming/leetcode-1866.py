class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        dp = {}

        def dfs(N, K):
            if N == K:
                return 1
            if N == 0 or K == 0:
                return 0
            if (N, K) in dp:
                return dp[(N, K)]

            dp[(N, K)] = (dfs(N - 1, K - 1)  # 最长的放在最右边, 所以最长的肯定能看到， n-1, k-1
                          + (N - 1) * dfs(N - 1, K))  # 除开最长的，剩下N-1个中任选一个放在最右边，最右边的肯定不能被看到， n-1, k
            return dp[(N, K)]

        return dfs(n, k) % (10 ** 9 + 7)

    def rearrangeSticksV2(self, n: int, k: int) -> int:
        dp = {(1, 1): 1}

        for N in range(2, n + 1):
            for K in range(1, k + 1):
                dp[(N, K)] = (dp.get((N - 1, K - 1), 0) +
                              (N - 1) * dp.get((N - 1, K), 0))
        return dp[(n, k)] % (10 ** 9 + 7)


if __name__ == '__main__':
    n = 3
    k = 2

    solu = Solution()
    a = solu.rearrangeSticks(n, k)
    print(a)

    n = 5
    k = 5
    a = solu.rearrangeSticks(n, k)
    print(a)

    n = 20
    k = 11
    a = solu.rearrangeSticks(n, k)
    print(a)

    a = solu.rearrangeSticksV2(n, k)
    print(a)
