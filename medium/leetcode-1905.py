from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        visited = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                    grid2[r][c] == 0 or (r, c) in visited):
                return True
            visited.add((r, c))
            res = True
            if grid1[r][c] == 0:
                res = False

            res = dfs(r, c + 1) and res
            res = dfs(r + 1, c) and res
            res = dfs(r, c - 1) and res
            res = dfs(r - 1, c) and res
            return res

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] and (r, c) not in visited and dfs(r, c):
                    count += 1
        return count


if __name__ == '__main__':
    grid1 = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]]
    grid2 = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
    s = Solution()
    a = s.countSubIslands(grid1, grid2)
    print(a)
