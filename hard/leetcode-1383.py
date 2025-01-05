import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = []
        for eff, spd in zip(efficiency, speed):
            eng.append([eff, spd])
        eng.sort(reverse=True)  # 根据 eff 降序排列
        # print(eng)
        res, speed = 0, 0
        minHeap = []  # 存放的 spd
        for eff, spd in eng:  # 每次选中的 eff, 都是截至到目前位置最小的,因为前面根据eff降序排列了
            if len(minHeap) == k:
                speed -= heapq.heappop(minHeap)  # 每次出栈的,对应的eff肯定比当前eff 大,我们需要选最小的eff,所以不用考虑出栈spd对应的eff

            speed += spd
            heapq.heappush(minHeap, spd)
            res = max(res, eff * speed)
        return res % (10 ** 9 + 7)


if __name__ == '__main__':
    s = Solution()
    n = 6
    speed = [2, 10, 3, 1, 5, 8]
    efficiency = [5, 4, 3, 9, 7, 2]
    k = 2
    a = s.maxPerformance(n, speed, efficiency, k)
    print(a)

    n = 6
    speed = [2, 10, 3, 1, 5, 8]
    efficiency = [5, 4, 3, 9, 7, 2]
    k = 3
    a = s.maxPerformance(n, speed, efficiency, k)
    print(a)

    n = 6
    speed = [2, 10, 3, 1, 5, 8]
    efficiency = [5, 4, 3, 9, 7, 2]
    k = 4
    a = s.maxPerformance(n, speed, efficiency, k)
    print(a)
