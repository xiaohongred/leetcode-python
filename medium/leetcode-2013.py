from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if abs(py - y) != abs(px - x) or x == px or y == py:
                continue
            res += (self.ptsCount[(x, py)] * self.ptsCount[(px, y)])
        return res


if __name__ == '__main__':
    detectSquares = DetectSquares()
    detectSquares.add([3, 10]);
    detectSquares.add([11, 2]);
    detectSquares.add([3, 2]);
    c = detectSquares.count([11, 10])
    print(c)
    c = detectSquares.count([14, 8])
    print(c)
    detectSquares.add([11, 2])

    c = detectSquares.count([11, 10])
    print(c)
    print(c)
    point = [0, 0]
    detectSquares.add(point)
    param_2 = detectSquares.count(point)
