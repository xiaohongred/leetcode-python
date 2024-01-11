from typing import (
    List,
)

# https://www.lintcode.com/problem/919/

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        start = [i.start for i in intervals]
        start = sorted(start)

        end = sorted([i.end for i in intervals])
        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res


if __name__ == '__main__':
    intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    s = Solution()
    a = s.min_meeting_rooms(intervals)
    print(a)
