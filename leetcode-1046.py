import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 使用最大堆
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first == second:
                continue
            if first != second:
                res = -1 * abs(abs(first) - abs(second))
                heapq.heappush(stones, res)

        if len(stones) == 0:
            return 0

        return abs(heapq.heappop(stones))


if __name__ == '__main__':
    pass