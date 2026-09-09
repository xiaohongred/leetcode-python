from typing import List
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        numsLen = len(nums)
        ans = [0] * numsLen
        K = 2*k
        total = 0
        for i, n in enumerate(nums):
            if k == 0:
                ans[i] = n
                continue
            left = i - k
            right = i + k
            if right >= numsLen:
                ans[i] = -1
                continue
            total += n
            total += nums[right]
            if left < 0:
                ans[i] = -1
                continue
            if left >= numsLen:
                ans[i] = -1
                continue
            ans[i] = (total-n) // (2*k + 1)
            total -= nums[left]
            total -= n
        return ans

    def getAveragesV2(self, nums: List[int], k: int) -> List[int]:
        avgs = [-1] * len(nums)
        s = 0  # 维护窗口元素和
        for i, x in enumerate(nums):
            # 1. 进入窗口
            s += x
            if i < k * 2:  # 窗口大小不足 2k+1
                continue
            # 2. 记录答案
            avgs[i - k] = s // (k * 2 + 1)
            # 3. 离开窗口
            s -= nums[i - k * 2]
        return avgs

if __name__ == "__main__":
    solution = Solution()
    nums = [7,4,3,9,1,8,5,2,6]
    k = 3
    result = solution.getAverages(nums, k)
    print(result)  # Output: [-1,-1,-1,5,4,4,-1,-1,-1]

    nums = [100000]
    k = 0
    result = solution.getAverages(nums, k)
    print(result)  # Output: [100000]

    nums = [8]
    k = 10000
    result = solution.getAverages(nums, k)
    print(result)  # Output: [-1]