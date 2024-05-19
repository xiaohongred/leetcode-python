from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        allSum = sum(nums)
        if allSum % k:
            return False
        targetVal = allSum / k
        nums.sort(reverse=True)
        used = [False] * len(nums)

        def backtrack(i, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == targetVal:
                return backtrack(0, k - 1, 0)

            for j in range(i, len(nums)):
                if subsetSum + nums[j] > targetVal or used[j]:
                    continue
                used[j] = True
                if backtrack(j + 1, k, subsetSum + nums[j]):
                    return True
                used[j] = False
            return False

        return backtrack(0, k, 0)

    def canPartitionKSubsetsV2(self, nums: List[int], k: int) -> bool:
        cur = [0] * k

        def dfs(i):
            if i == len(nums):
                return True
            for j in range(k):
                if j and cur[j] == cur[j - 1]:
                    continue
                cur[j] += nums[i]
                if cur[j] <= s and dfs(i + 1):
                    return True
                cur[j] -= nums[i]
            return False

        s, mod = divmod(sum(nums), k)
        if mod:
            return False
        nums.sort(reverse=True)
        return dfs(0)


if __name__ == '__main__':
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4

    s = Solution()
    a = s.canPartitionKSubsets(nums, k)
    print(a)

    nums = [10, 1, 10, 9, 6, 1, 9, 5, 9, 10, 7, 8, 5, 2, 10, 8]
    k = 10
    a = s.canPartitionKSubsets(nums, k)
    print(a)

    nums = [9, 6, 1, 8, 4, 3, 4, 1, 7, 3, 7, 4, 5, 3, 2, 3]
    k = 10
    a = s.canPartitionKSubsets(nums, k)
    print(a)
