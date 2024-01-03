from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        leftBound = 0
        rightBound = col - 1

        topBound = 0
        lowBound = row - 1
        res = []
        while len(res) < row * col:
            # get every i in the topBound row
            if topBound <= lowBound:
                for i in range(leftBound, rightBound + 1):
                    res.append(matrix[topBound][i])
                topBound += 1

            # get every i in the rightBound col
            if leftBound <= rightBound:
                for i in range(topBound, lowBound + 1):
                    res.append(matrix[i][rightBound])
                rightBound -= 1

            # get every i in the bottom row
            if topBound <= lowBound:
                for i in range(rightBound, leftBound - 1, -1):
                    res.append(matrix[lowBound][i])
                lowBound -= 1

            # get every i in the left col
            if leftBound <= rightBound:
                for i in range(lowBound, topBound - 1, -1):
                    res.append(matrix[i][leftBound])
                leftBound += 1
        return res


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s = Solution()
    a = s.spiralOrder(matrix)
    print(a)
