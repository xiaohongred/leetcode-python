from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # brute force
        res = 0
        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                a = min(height[l], height[r]) * (r - l)
                res = max(res, a)

        return res

    def maxAreaV2(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            a = min(height[l], height[r]) * (r - l)
            res = max(a, res)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res


if __name__ == '__main__':
    num = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    a = s.maxArea(num)
    print(a)

    a = s.maxAreaV2(num)
    print(a)
