from typing import List


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        board[rMove][cMove] = color
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1],
                     [1, 1], [-1, -1], [1, -1], [-1, 1]]

        def legal(row, col, color, direc):
            dr, dc = direc
            row, col = row + dr, col + dc
            length = 1
            while 0 <= row < ROWS and 0 <= col < COLS:
                length += 1
                if board[row][col] == ".":
                    return False
                if board[row][col] == color:
                    return length >= 3

                row, col = row + dr, col + dc
            return False

        for dir in direction:
            if legal(rMove, cMove, color, dir):
                return True
        return False


if __name__ == '__main__':
    board = [[".", ".", ".", "c", ".", ".", ".", "."],
             [".", ".", ".", "W", ".", ".", ".", "."],
             [".", ".", ".", "W", ".", ".", ".", "."],
             [".", ".", ".", "W", ".", ".", ".", "."],
             ["W", "B", "B", ".", "W", "W", "W", "B"],
             [".", ".", ".", "B", ".", ".", ".", "."],
             [".", ".", ".", "B", ".", ".", ".", "."],
             [".", ".", ".", "W", ".", ".", ".", "."]]
    rMove = 4
    cMove = 3
    color = "B"

    s = Solution()
    a = s.checkMove(board, rMove, cMove, color)
    print(a)
