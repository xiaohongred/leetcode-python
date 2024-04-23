import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visited = set()
        minHeap = [[grid[0][0], 0, 0]]  # (time, r, c)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited.add((0, 0))
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            visited.add((r, c))
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or
                        neiR == N or neiC == N or
                        (neiR, neiC) in visited):
                    continue
                visited.add((neiR, neiC))
                heapq.heappush(minHeap, [max(t, grid[neiR][neiC]), neiR, neiC])


if __name__ == '__main__':
    grid = [[0, 2], [1, 3]]
    s = Solution()
    a = s.swimInWater(grid)
    print(a)

    grid = [[0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6]]

    a = s.swimInWater(grid)
    print(a)
