from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []  # pair [num, minLeft] mono decreasing
        curMin = nums[0]
        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and stack[-1][0] > n > stack[-1][1]:
                # 需要满足 i < j < k 和 nums[i] < nums[k] < nums[j]
                # n 相当于是 nums[k],  stack[-1][1] 是 minLeft， 相当于上面的 nums[i]， stack[-1][0]相当于 nums[j]
                return True
            stack.append([n, curMin])
            curMin = min(curMin, n)
        return False

    def find132patternV1(self, nums: List[int]) -> bool:
        stack = []  # pair [num, minLeft] mono decreasing,   minLeft 是 值为 num 的数在 nums数组中左边的最小值
        curMin = nums[0]
        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and stack[-1][1] < n < stack[-1][0]:  # 感觉这样写更容易比较
                # 需要满足 i < j < k 和 nums[i] < nums[k] < nums[j]
                # n 相当于是 nums[k],
                # stack[-1][1] 是 minLeft， 相当于上面的 nums[i]，
                # stack[-1][0]相当于 nums[j]
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

    nums = [-1, 3, 2, 0]
    a = s.find132pattern(nums)
    print(a)

    nums = [1, 2, 3, 4]
    a = s.find132patternV1(nums)
    print(a)

    nums = [3, 1, 4, 2]
    a = s.find132patternV1(nums)
    print(a)

    nums = [-1, 3, 2, 0]
    a = s.find132patternV1(nums)
    print(a)
