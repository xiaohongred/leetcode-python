import collections
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # for each pt determine if it lies on the longest line
        # count all pts with same slope
        # update result with max
        res = 1
        for i in range(len(points)):
            p1 = points[i]
            count = collections.defaultdict(int)
            for j in range(i + 1, len(points)):
                p2 = points[j]
                if p2[0] == p1[0]:
                    slope = float("inf")
                else:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                count[slope] += 1
                res = max(res, count[slope] + 1)
        return res


if __name__ == '__main__':
    s = Solution()
    points = [[1, 1], [2, 2], [3, 3]]
    a = s.maxPoints(points)
    print(a)

    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    a = s.maxPoints(points)
    print(a)
