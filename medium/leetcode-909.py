from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)

        board.reverse()  # 底部是第0行

        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 - c
            return [r, c]

        q = deque()  # [square, moves]
        q.append([1, 0])
        visited = set()
        visited.add(1)
        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]

                if nextSquare == length * length:
                    return moves + 1
                if nextSquare not in visited:
                    visited.add(nextSquare)
                    q.append([nextSquare, moves + 1])
        return -1


if __name__ == '__main__':
    board = [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1],
             [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]
    s = Solution()
    a = s.snakesAndLadders(board)
    print(a)
