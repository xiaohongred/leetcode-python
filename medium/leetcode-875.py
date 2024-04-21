import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxP = max(piles)
        l = 1
        r = maxP
        res = r
        while l <= r:
            k = (l + r) // 2
            sumH = 0
            for p in piles:
                sumH += math.ceil(p / k)
            if sumH <= h:
                r = k - 1
                res = min(k, res)
            else:
                l = k + 1

        return res


if __name__ == '__main__':
    piles = [3, 6, 7, 11]
    h = 8
    s = Solution()
    a = s.minEatingSpeed(piles, h)
    print(a)
