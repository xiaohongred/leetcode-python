import heapq


class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)
        self.data.sort()

    def findMedian(self) -> float:
        length = len(self.data)
        if length % 2 == 0:
            return (self.data[length // 2] + self.data[length // 2 - 1]) / 2
        else:
            return self.data[len(self.data) // 2]


class MedianFinderV2:

    def __init__(self):
        # two heaps,
        # large,   small,
        # minheap, maxheap  python中没有maxheap, 所以需要乘-1来模拟
        # heaps should be equal size
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        # make sure every num small is <= every num in large
        if (self.small and self.large and
                (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # uneven size?
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2


if __name__ == '__main__':
    s = MedianFinder()
    # s = MedianFinderV2()
    s.addNum(1)
    s.addNum(1)
    a = s.findMedian()
    print(a)
    s.addNum(3)
    s.addNum(4)
    a = s.findMedian()
    print(a)
