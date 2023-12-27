from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        rowFlag = [0 for _ in range(m)]
        colFlag = [0 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rowFlag[i] = 1
                    colFlag[j] = 1

        for i in range(m):
            if rowFlag[i] == 1:
                for k in range(n):
                    matrix[i][k] = 0

        for j in range(n):
            if colFlag[j] == 1:
                for k in range(m):
                    matrix[k][j] = 0

    def setZeroesV2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:  # zero first row if need
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero == True:  # zero firt row if need
            for c in range(COLS):
                matrix[0][c] = 0


if __name__ == '__main__':
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    s = Solution()
    s.setZeroes(matrix)
    print(matrix)
