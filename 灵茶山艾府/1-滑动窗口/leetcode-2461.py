from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        mySet = {}
        ans = 0
        total = 0
        for i, n in enumerate(nums):
            left = i - k + 1
            total += n
            mySet[n] = mySet.get(n, 0) + 1

            if left < 0:
                continue
            
            if len(mySet) == k:
                ans = max(total, ans)

            total -= nums[left]
            mySet[nums[left]] -= 1 
            if mySet[nums[left]] == 0:
                del  mySet[nums[left]] 

        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.maximumSubarraySum([1,5,4,2,9,9,9], 3))

    nums = [4,4,4]
    k = 3
    print(s.maximumSubarraySum(nums, k))