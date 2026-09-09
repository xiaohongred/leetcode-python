from typing import List
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        ans = float("-inf")
        total = 0
        mySet = {}
        for i, n in enumerate(nums):
            left = i - k + 1
            total += n
            mySet[n] = mySet.get(n, 0) + 1
            if left < 0:
                continue
            
            if len(mySet) >= m:
                ans = max(ans, total)
            total -= nums[left]
            mySet[nums[left]] = mySet[nums[left]] -  1
            if mySet[nums[left]] == 0:
                del mySet[nums[left]]
        return 0 if ans == float("-inf") else ans



if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,4,5]
    m = 3
    k = 3
    result = solution.maxSum(nums, m, k)
    print(result)  # Output: 12

    nums = [1,2,3,4,5]
    m = 3
    k = 2
    result = solution.maxSum(nums, m, k)
    print(result)  # Output: 0

    nums = [1,2,3,4,5]
    m = 1
    k = 1
    result = solution.maxSum(nums, m, k)
    print(result)  # Output: 5