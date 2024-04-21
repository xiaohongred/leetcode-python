import math
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        minReach = []
        for d, s in zip(dist, speed):
            minute = math.ceil(d / s)  # d=3, s=2, 3/2 = 2
            minReach.append(minute)
        minReach.sort()
        res = 0
        for minute in range(len(minReach)):
            if minute >= minReach[minute]:
                return res
            res += 1
        return res


if __name__ == '__main__':
    dist = [1, 3, 4]
    speed = [1, 1, 1]
    s = Solution()
    a = s.eliminateMaximum(dist, speed)
    print(a)
