import heapq
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        totalLen = len(hand)
        if totalLen % groupSize:
            return False
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        minHeap = list(count.keys())
        heapq.heapify(minHeap)
        while minHeap:
            first = minHeap[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        totalLen = len(nums)
        if totalLen % k:
            return False
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        minHeap = list(count.keys())
        heapq.heapify(minHeap)
        while minHeap:
            first = minHeap[0]
            for i in range(first, first + k):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True


if __name__ == '__main__':
    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize = 3
    s = Solution()
    a = s.isNStraightHand(hand, groupSize)
    print(a)
