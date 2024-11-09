from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        rows = m

        n = len(matrix[0])
        cols = n

        top, bot = 0, rows - 1

        while top <= bot:
            midRow = (top + bot) // 2  # 判断 target 有没有可能在 midRow 这一行
            if target > matrix[midRow][-1]:  # target 肯定在 midRow 这一行以下的行
                top = midRow + 1
            elif target < matrix[midRow][0]:  # target 肯定在 midRow 这一行以上的行
                bot = midRow - 1
            else:
                # 判断 target 有可能在 midRow 这一行,退出通过行来筛选的过程
                break  # break this loop, because we can not divide this matrix by rows

        if not (top <= bot):
            return False
        row = (top + bot) // 2

        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3

    a = s.searchMatrix(matrix, target)
    print(a)

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    a = s.searchMatrix(matrix, target)
    print(a)
