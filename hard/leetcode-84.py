from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:  # stack 是一个按照矩形高度递增的栈
                # 遇到高度减小的情况了，计算
                preIndex, preHeight = stack.pop()
                maxArea = max(maxArea, preHeight * (i - preIndex))
                start = preIndex
            # 如果 stack[-1][1] <= h, 直接入栈
            stack.append((start, h))
        for i, h in stack:  # 剩余的 stack 中是递增的, 计算从每个位置扩展到最后位置形成的矩形面积
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


if __name__ == '__main__':
    s = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    a = s.largestRectangleArea(heights)
    print(a)

    heights = [2, 4]
    a = s.largestRectangleArea(heights)
    print(a)
