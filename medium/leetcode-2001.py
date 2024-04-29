from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        rate = []
        for rec in rectangles:
            rate.append(float(rec[0]) / float(rec[1]))

        myMap = {}
        res = 0
        for r in rate:
            if r in myMap.keys():
                myMap[r] = myMap[r] + 1
            else:
                myMap[r] = 1
        for k, m in myMap.items():
            res += (m * (m - 1) / 2)
        return int(res)

    def interchangeableRectanglesV2(self, rectangles: List[List[int]]) -> int:
        count = {}
        for w, h in rectangles:
            count[w / h] = 1 + count.get(w / h, 0)

        res = 0
        for c in count.values():
            if c > 1:
                res += (c * (c - 1) // 2)
        return res


if __name__ == '__main__':
    rectangles = [[4, 8], [3, 6], [10, 20], [15, 30]]
    s = Solution()
    a = s.interchangeableRectangles(rectangles)
    print(a)

    rectangles = [[4, 5], [7, 8]]
    a = s.interchangeableRectanglesV2(rectangles)
    print(a)
