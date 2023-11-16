import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.myNums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.myNums.append(val)
        self.myNums.sort()
        return self.myNums[len(self.myNums) - 1 - (self.k - 1)]


class KthLargestV2:
    def __init__(self, k: int, nums: List[int]):
        self.minKHeap = nums
        self.k = k

        heapq.heapify(self.minKHeap)
        while len(self.minKHeap) > k:
            heapq.heappop(self.minKHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minKHeap, val)
        if len(self.minKHeap) > self.k:
            heapq.heappop(self.minKHeap)

        return self.minKHeap[0]


if __name__ == '__main__':
    pass
