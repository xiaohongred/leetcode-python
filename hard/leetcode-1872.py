from itertools import accumulate
from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        pre = list(accumulate(stones))

        n = len(stones)

        f = [0] * n # 设 f(i) 表示当 Alice 可以选择的下标 u 在 [i,n) 范围内时，Alice 与 Bob 分数的最大差值

        f[n-1] = pre[n-1]
        for i in range(n-2, 0, -1):
            f[i] = max(f[i+1], pre[i] - f[i+1])
        return f[1] # 选择一个整数 x > 1 ，并且 移除 最左边的 x 个石子  所以应该从第二个开始


if __name__ == '__main__':
    so = Solution()
    stones = [-1, 2, -3, 4, -5]
    print(so.stoneGameVIII(stones))

    stones = [7,-6,5,10,5,-2,-6]
    print(so.stoneGameVIII(stones))