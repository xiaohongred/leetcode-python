import heapq
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])
        minHeap = []  # pair of [end, numPassengers]
        curPass = 0
        for t in trips:
            numPass, start, end = t
            while minHeap and minHeap[0][0] <= start:
                curPass -= minHeap[0][1]
                heapq.heappop(minHeap)
            curPass += numPass
            if curPass > capacity:
                return False
            heapq.heappush(minHeap, [end, numPass])
        return True

    def carPoolingV2(self, trips: List[List[int]], capacity: int) -> bool:
        passChange = [0] * 1001
        for t in trips:
            numPass, start, end = t
            passChange[start] += numPass
            passChange[end] -= numPass
        curPass = 0
        for i in range(1001):
            curPass += passChange[i]
            if curPass > capacity:
                return False
        return True


if __name__ == '__main__':
    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 4

    s = Solution()
    a = s.carPooling(trips, capacity)
    print(a)
