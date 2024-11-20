from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # maxLeft, maxRight
        # min(maxLeft, maxRight) - h[i]
        maxLeft = [0]
        curMaxLeft = height[0]
        for index in range(1, len(height)):
            maxLeft.append(curMaxLeft)
            curMaxLeft = max(curMaxLeft, height[index])

        maxRight = [0]
        curMaxRight = height[-1]
        for index in range(len(height) - 2, -1, -1):
            maxRight.append(curMaxRight)
            curMaxRight = max(curMaxRight, height[index])
        maxRight = maxRight[::-1]

        res = 0
        for i in range(len(height)):
            cur = min(maxRight[i], maxLeft[i]) - height[i]
            if cur <= 0:
                continue
            else:
                res += cur
        return res

    def trapV2(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += max(leftMax - height[l], 0)
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += max(rightMax - height[r], 0)
        return res


if __name__ == '__main__':
    s = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    a = s.trap(height)
    print(a)

    height = [4, 2, 0, 3, 2, 5]
    a = s.trap(height)
    print(a)

    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    a = s.trapV2(height)
    print(a)

    height = [4, 2, 0, 3, 2, 5]
    a = s.trapV2(height)
    print(a)
