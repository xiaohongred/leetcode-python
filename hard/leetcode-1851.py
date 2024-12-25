import heapq
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = sorted(intervals, key=lambda x: x[0])
        minHeap = []
        res, i = {}, 0  # res  ｛q:minLenInterval｝
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:  # 没有完全理解
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]


if __name__ == '__main__':
    s = Solution()
    intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
    queries = [2, 3, 4, 5]
    a = s.minInterval(intervals, queries)
    print(a)

    intervals = [[2, 3], [2, 5], [1, 8], [20, 25]]
    queries = [2, 19, 5, 22]
    a = s.minInterval(intervals, queries)
    print(a)
