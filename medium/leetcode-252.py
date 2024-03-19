from typing import (
    List,
)

"""
Definition of Interval:

"""


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


# https://www.lintcode.com/problem/920/description
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]
            if i1.end > i2.start:
                return False

        return True


if __name__ == '__main__':
    intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    s = Solution()
    a = s.can_attend_meetings(intervals)
    print(a)
