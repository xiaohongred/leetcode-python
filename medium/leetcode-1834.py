import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t: t[0])
        res, minHeap = [], []
        i, time = 0, tasks[0][0]
        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1
            if not minHeap:
                # minHeap is empty, fastforward time to next task enqueueTime
                time = tasks[i][0]
            else:
                procTime, index = heapq.heappop(minHeap)
                time += procTime
                res.append(index)
        return res


if __name__ == '__main__':
    tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]
    s = Solution()
    a = s.getOrder(tasks)
    print(a)
