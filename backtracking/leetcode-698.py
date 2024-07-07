from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        numSum = sum(nums)
        target = numSum / k
        if numSum % k:
            return False

        used = [False] * len(nums)

        def backtrack(i, k, curSubsetSum):
            if k == 0:
                return True
            if curSubsetSum == target:
                return backtrack(0, k - 1, 0)
            for j in range(i, len(nums)):
                if used[j] or nums[j] + curSubsetSum > target:
                    continue
                used[j] = True
                if backtrack(j + 1, k, curSubsetSum + nums[j]):
                    return True
                used[j] = False
            return False

        return backtrack(0, k, 0)

    def canPartitionKSubsetsV2(self, nums: List[int], k: int):
        cur = [0] * k
        target, mod = divmod(sum(nums), k)
        if mod:
            return False
        nums.sort()

        def dfs(i):
            if i == len(nums):
                return True

            for j in range(k):
                if j != 0 and cur[j] == cur[j - 1]:
                    continue

                cur[j] += nums[i]
                if cur[j] <= target and dfs(i + 1):
                    return True
                cur[j] -= nums[i]
            return False

        return dfs(0)


if __name__ == '__main__':
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4

    s = Solution()
    a = s.canPartitionKSubsets(nums, k)
    print(a)

    nums = [1, 2, 3, 4]
    k = 3
    a = s.canPartitionKSubsets(nums, k)
    print(a)
