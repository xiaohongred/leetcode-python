from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        direct = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        def invalid(r, c):
            if r < 0 or c < 0 or r == n or c == n:
                return True
            return False

        visited = set()

        def dfs(r, c):
            if (invalid(r, c) or not grid[r][c] or (r, c) in visited):
                return
            visited.add((r, c))
            for dr, dc in direct:
                dfs(r + dr, c + dc)

        def bfs():
            res = 0
            q = deque(visited)
            while q:
                curQLen = len(q)
                for i in range(curQLen):
                    r, c = q.popleft()
                    for dr, dc in direct:
                        curR, curC = r + dr, c + dc
                        if invalid(curR, curC) or (curR, curC) in visited:
                            continue
                        if grid[curR][curC]:
                            return res
                        q.append([curR, curC])
                        visited.add((curR, curC))
                res += 1
            return res

        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()


if __name__ == '__main__':
    grid = [[0, 1], [1, 0]]

    s = Solution()
    a = s.shortestBridge(grid)
    print(a)

    grid = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
    a = s.shortestBridge(grid)
    print(a)

    grid = [[1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]]
    a = s.shortestBridge(grid)
    print(a)
