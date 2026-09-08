from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix) # n行
        m = len(matrix[0]) # m列
        result = [[0] * n for _ in range(m)] # m行n列的矩阵
        for i in range(n):
            for j in range(m):
                result[j][i] = matrix[i][j]
        return result

if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    result = solution.transpose(matrix)
    print(result)  # Output: [[1,4,7],[2,5,8],[3,6,9]]

    matrix = [[1,2,3],[4,5,6]]
    result = solution.transpose(matrix)
    print(result)  # Output: [[1,4],[2,5],[3,6]]