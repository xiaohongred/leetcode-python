from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.preSumMat = [[0] * (cols + 1) for c in range(rows + 1)]
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.preSumMat[r][c + 1]
                self.preSumMat[r + 1][c + 1] = prefix + above  # self.preSumMat 中第一行，第一列都为0

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.preSumMat[row2][col2]
        above = self.preSumMat[row1 - 1][col2]
        left = self.preSumMat[row2][col1 - 1]
        topleft = self.preSumMat[row1 - 1][col1 - 1]
        return bottomRight - above - left + topleft


if __name__ == '__main__':
    matrix = [[3, 0, 1, 4, 2],
              [5, 6, 3, 2, 1],
              [1, 2, 0, 1, 5],
              [4, 1, 0, 1, 7],
              [1, 0, 3, 0, 5]]
    nm = NumMatrix(matrix)
    print(nm.preSumMat)
