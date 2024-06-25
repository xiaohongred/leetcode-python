from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= row or
                    c >= col or word[i] != board[r][c] or
                    (r, c) in path):
                return False
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1)
                   )
            path.remove((r, c))
            return res

        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    word = "ABCCED"
    s = Solution()
    a = s.exist(board, word)
    print(a)

    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    word = "SEE"
    a = s.exist(board, word)
    print(a)

    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    word = "ABCB"
    a = s.exist(board, word)
    print(a)
