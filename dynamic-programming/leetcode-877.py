from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # 5,3,4,5    偶数堆石子, 石子的 总数 是 奇数
        dp = {}  # subarr piles (l, r) -> max alice total

        # return: max alice total
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            # 模拟 alice 选择和 bob选择的情况
            res = max(piles[l] + dfs(l + 2, r),  # alice 选择左边 且之后bob也选择左边
                      piles[l] + dfs(l + 1, r - 1),  # alice 选择左边 之后bob选择右边
                      piles[r] + dfs(l, r - 2),  # alice 选择右边 且之后bob也选择右边
                      piles[r] + dfs(l + 1, r - 1))  # alice 选择右边 之后bob选择左边
            dp[(l, r)] = res
            return res

        total = sum(piles)
        print(dfs(0, len(piles) - 1))
        return dfs(0, len(piles) - 1) > total / 2

    def stoneGameV2(self, piles: List[int]) -> bool:
        # 5,3,4,5    偶数堆石子, 石子的总数是奇数
        dp = {}  # subarr piles (l, r) -> max alice total

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            even = True if (r - l) % 2 else False
            # 只有石子堆数是偶数时， alice 才能选择 因为 alice 先选择
            left = piles[l] if even else 0
            right = piles[r] if even else 0
            dp[(l, r)] = max(dfs(l + 1, r) + left, dfs(l, r - 1) + right)
            return dp[(l, r)]

        total = sum(piles)
        print(dfs(0, len(piles) - 1))
        return dfs(0, len(piles) - 1) > total / 2


if __name__ == '__main__':
    piles = [5, 3, 4, 5]
    s = Solution()
    a = s.stoneGame(piles)
    a = s.stoneGameV2(piles)
    print(a)
