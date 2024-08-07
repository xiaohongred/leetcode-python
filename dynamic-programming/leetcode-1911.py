from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}

        # i = index, even = true/false, total = current sum
        def dfs(i, even):
            if i == len(nums):
                return 0
            if (i, even) in dp:
                return dp[(i, even)]
            total = nums[i] if even else (-1 * nums[i])  # 如果当前索引 i 在子序列中是偶数，则需要加上nums[i], 如果是奇数，就减去nums[i]
            dp[(i, even)] = max(total + dfs(i + 1, not even),  # 选择当前索引 i, 并且下一个选择的索引位置，奇偶性改变
                                dfs(i + 1, even))  # 不选择当前索引，并且下一个选择索引位置，奇偶性不变
            return dp[(i, even)]

        return dfs(0, True)

    def maxAlternatingSumDP(self, nums: List[int]) -> int:
        sumEven, sumOdd = 0, 0
        for i in range(len(nums) - 1, -1, -1):
            # 从后网前遍历， 从i 到 len(nums) - 1 的区间中，子数组的交替和分别是 sumEven -> i在子数组中是偶数，
            #                                                           sumOdd -> i在子数组中是奇数
            tmpEven = max(sumOdd + nums[i], sumEven)
            tmpOdd = max(sumEven - nums[i], sumOdd)

            sumEven, sumOdd = tmpEven, tmpOdd
        return sumEven


if __name__ == '__main__':
    nums = [4, 2, 5, 3]
    s = Solution()
    a = s.maxAlternatingSum(nums)
    print(a)

    a = s.maxAlternatingSumDP(nums)
    print(a)

    nums = [5, 6, 7, 8]
    a = s.maxAlternatingSum(nums)
    print(a)

    a = s.maxAlternatingSumDP(nums)
    print(a)

    nums = [6, 2, 1, 2, 4, 5]
    a = s.maxAlternatingSum(nums)
    print(a)

    a = s.maxAlternatingSumDP(nums)
    print(a)
