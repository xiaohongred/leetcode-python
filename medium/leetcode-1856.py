from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        res = 0

        stack = []  # [(start, val), (start, val)]
        prefix = [0]

        for n in nums:
            prefix.append(prefix[-1] + n)

        for i, n in enumerate(nums):
            newStart = i
            while stack and stack[-1][1] > n:
                start, val = stack.pop()
                total = prefix[i] - prefix[start]  # 注意这里 i 已经是下一个值了，所以在prefix[i] 中是正确的
                res = max(res, val * total)
                newStart = start
            stack.append((newStart, n))
        for start, val in stack:
            total = prefix[len(nums)] - prefix[start]  # prefix 数组比 nums右移了一位，所以不需要 len(nums) - 1
            res = max(res, total * val)
        return res % (10 ** 9 + 7)


if __name__ == '__main__':
    nums = [1, 2, 3, 2]
    s = Solution()
    a = s.maxSumMinProduct(nums)
    print(a)
