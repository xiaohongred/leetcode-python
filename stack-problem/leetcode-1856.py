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
                total = prefix[i] - prefix[start]
                res = max(res, val * total)
                newStart = start
            stack.append((newStart, n))

        for start, val in stack:
            total = prefix[len(nums)] - prefix[start]
            res = max(res, total * val)
        return res % (10 ** 9 + 7)


if __name__ == '__main__':
    nums = [1, 2, 3, 2]
    s = Solution()
    a = s.maxSumMinProduct(nums)
    print(a)

    nums = [2, 3, 3, 1, 2]
    a = s.maxSumMinProduct(nums)
    print(a)

    nums = [3, 1, 5, 6, 4, 2]
    a = s.maxSumMinProduct(nums)
    print(a)
