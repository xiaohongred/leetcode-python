from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)
        for i, h in enumerate(heights):
            start = i
            while start and stack[-1][1] > h:
                preIndex, preHeight = stack.pop()
                maxArea = max(maxArea, preHeight * (i - preIndex))  # (i - preIndex) 代表 preHeight 可以组成矩阵的宽度
                start = preIndex
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    s = Solution()
    a = s.largestRectangleArea(heights)
    print(a)

    heights = [2, 4]
    a = s.largestRectangleArea(heights)
    print(a)
