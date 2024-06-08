from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: (i[0], -i[1]))

        res = [intervals[0]]
        for l, r in intervals[1:]:
            prevL, prevR = res[-1]

            if prevL <= l and prevR >= r:
                continue
            res.append((l, r))
        return len(res)


if __name__ == '__main__':
    intervals = [[1, 4], [3, 6], [2, 8]]
    s = Solution()
    a = s.removeCoveredIntervals(intervals)
    print(a)
