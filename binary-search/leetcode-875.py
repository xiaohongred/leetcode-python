from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res


if __name__ == '__main__':
    s = Solution()
    piles = [3, 6, 7, 11]
    h = 8
    a = s.minEatingSpeed(piles, h)
    print(a)

    piles = [30, 11, 23, 4, 20]
    h = 5
    a = s.minEatingSpeed(piles, h)
    print(a)

    piles = [30, 11, 23, 4, 20]
    h = 6
    a = s.minEatingSpeed(piles, h)
    print(a)
