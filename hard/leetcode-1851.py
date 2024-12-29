import heapq
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = sorted(intervals, key=lambda x: x[0])
        minHeap = []  # (interval size,  interval right val)
        res, i = {}, 0  # res  ｛q:minLenInterval｝
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:  # 没有完全理解
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            # 在这之前，minHeap 中的interval ， intervals[i][0] <= q  都满足条件
            while minHeap and minHeap[0][1] < q:  # 通过这个while循环去掉  minHeap[0][1] < q 的interval,也就是不包括q的interval
                # in this while loop , we remove all interval that does not contain this q point
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1  # 此时 minHeap 中剩下的interval 就都是包含q 的，并且最小堆中第一个就是结果
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
