import heapq
from collections import Counter
from collections import deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task 1 unit time
        # minimize idle time
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]

        heapq.heapify(maxHeap)
        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)  # 这里相当于处理了一个字符
                if cnt:  # 如果处理了这个字符， 这个字符还存在（只是数量减少了），需要入队
                    q.append([cnt, time + n])  # cnt 的绝对值代表这个字符还有几个, time+n代表下次可以处理这个字符的时间
            print("time: ", time)
            print("--------------------")
            print(q)

            if q and q[0][1] <= time:  # q[0][1] <= time, 成立，代表到time+1时间时（也就是下次循环）可以再次处理之前已经处理过的字符串
                heapq.heappush(maxHeap, q.popleft()[0])  # 这里并不算处理，只是加入到堆中，说明下次循环可以处理这个字符了
            print("+++++++++++++++++++++")
            print(q)
            print("\n")
            print("\n")
        return time


if __name__ == '__main__':
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2

    s = Solution()
    a = s.leastInterval(tasks, n)
    print(a)

    tasks = ["A", "A", "A", "B", "B", "C", "C"]
    n = 1
    a = s.leastInterval(tasks, n)
    print(a)
