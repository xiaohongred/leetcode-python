from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = float("-inf")
        total = 0
        for i, n in enumerate(nums):
            left = i - k + 1
            total += n

            if left < 0:
                continue
            
            ans = max(ans, total*1.0 / k)

            total -= nums[left]
        return ans



if __name__ == "__main__":
    solution = Solution()
    nums = [1,12,-5,-6,50,3]
    k = 4
    result = solution.findMaxAverage(nums, k)
    print(result)  # Output: 12.75

    nums = [5]
    k = 1
    result = solution.findMaxAverage(nums, k)
    print(result)  # Output: 5.0