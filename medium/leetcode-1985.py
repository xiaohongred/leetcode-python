import heapq
from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        maxHeap = [-1 * int(n) for n in nums]
        heapq.heapify(maxHeap)
        res = None
        while k > 0:
            res = heapq.heappop(maxHeap)
            k -= 1

        return str(-1 * res)


if __name__ == '__main__':
    nums = ["3", "6", "7", "10"]
    k = 4
    s = Solution()
    a = s.kthLargestNumber(nums, k)
    print(a)
