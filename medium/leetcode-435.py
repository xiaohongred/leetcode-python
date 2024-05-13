from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
                continue
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        return res


if __name__ == '__main__':
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    s = Solution()
    a = s.eraseOverlapIntervals(intervals)
    print(a)

    intervals = [[1, 2], [1, 2], [1, 2]]
    a = s.eraseOverlapIntervals(intervals)
    print(a)
