from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        dp = {}

        def dfs(i, k):
            # dfs 返回值定义为 从 nums[i] 开始，把数组分成k份连续子数组（有不同种分法），
            #     不同分法中 连续子数组和的最大值 中的最小值
            if k == 1:
                return sum(nums[i:])
            if (i, k) in dp:
                return dp[(i, k)]

            res, curSum = float("inf"), 0
            for j in range(i, len(nums) - k + 1):
                curSum += nums[j]
                maxSum = max(curSum, dfs(j + 1, k - 1))  # 比较 curSum 与 剩下的不同分法的 连续数组最大和中的最小值的大小
                res = min(res, maxSum)
                if curSum > res:  # curSum 代表其中一个连续子数组的累加和
                    # 这个条件满足，就不需要再继续下去了，因为 curSum 大于 res 了，剩下的分法都不满足题目要求
                    break
            dp[(i, k)] = res
            return res

        return dfs(0, k)

    def splitArrayV2(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        def canSplit(largest):
            subarray = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarray += 1
                    curSum = n
            return (subarray + 1) <= k

        while l <= r:
            mid = (l + r) // 2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [7, 2, 5, 10, 8]
    k = 2
    a = s.splitArray(nums, k)
    print(a)

    nums = [1, 2, 3, 4, 5]
    k = 2
    a = s.splitArray(nums, k)
    print(a)

    nums = [1, 4, 4]
    k = 3
    a = s.splitArray(nums, k)
    print(a)

    nums = [7, 2, 5, 10, 8]
    k = 2
    a = s.splitArrayV2(nums, k)
    print(a)

    nums = [1, 2, 3, 4, 5]
    k = 2
    a = s.splitArrayV2(nums, k)
    print(a)

    nums = [1, 4, 4]
    k = 3
    a = s.splitArrayV2(nums, k)
    print(a)
