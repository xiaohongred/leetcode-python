from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # odd = [piles[i] for i in range(1, len(piles), 2)]
        # oushu = [piles[i] for i in range(0, len(piles), 2)]
        return True

    def stoneGameV2(self, piles: List[int]) -> bool:
        dp = {}  # subarr piles (l, r) -> max alice total

        allSum = sum(piles)

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            even = True if (r - l + 1) % 2 else False
            # 只有剩余石子堆的个数是偶数是， 才是alice选择
            left = piles[l] if even else 0
            right = piles[r] if even else 0

            dp[(l, r)] = max(dfs(l + 1, r) + left, dfs(l, r - 1) + right)
            return dp[(l, r)]

        aliceSum = dfs(0, len(piles) - 1)
        return aliceSum > (allSum // 2)


if __name__ == '__main__':
    piles = [5, 3, 4, 5]
    s = Solution()
    a = s.stoneGame(piles)
    print(a)
