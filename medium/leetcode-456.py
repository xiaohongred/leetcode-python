from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []  # pair [num, minLeft] mono decreasing
        curMin = nums[0]
        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and stack[-1][0] > n > stack[-1][1]:
                return True
            stack.append([n, curMin])
            curMin = min(curMin, n)
        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    s = Solution()
    a = s.find132pattern(nums)
    print(a)
    nums = [3, 1, 4, 2]
    a = s.find132pattern(nums)
    print(a)
