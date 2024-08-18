from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = []

        def getCurNum(i: int, j: int, prevrow: List[int]):
            if i < 0 and j >= len(prevrow):
                return 0
            if i >= 0 and j >= len(prevrow):
                return prevrow[i]
            if i >= 0 and j < len(prevrow):
                return prevrow[i] + prevrow[j]
            return prevrow[i] + prevrow[j]

        for r in range(numRows):
            if r == 0:
                res.append([1])
                continue
            rowLen = r + 1
            cols = []
            for c in range(rowLen):
                if c == 0:
                    cols.append(res[r - 1][0])
                    continue
                if c == rowLen - 1:
                    cols.append(res[r - 1][-1])
                    continue
                cols.append(getCurNum(c - 1, c, res[r - 1]))
            res.append(cols)
        return res

    def generateV2(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):  # 有 len(res[-1]) + 1 列
                row.append((temp[j] + temp[j + 1]))
            res.append(row)
        return res


if __name__ == '__main__':
    numRows = 5
    s = Solution()
    a = s.generate(numRows)
    print(a)

    a = s.generateV2(numRows)
    print(a)
