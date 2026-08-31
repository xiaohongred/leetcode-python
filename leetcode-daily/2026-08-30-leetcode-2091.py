from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        miniVal, maxVal = float('inf'), float('-inf')
        miniIndex, maxIndex = -1, -1
        n = len(nums)
        for i in range(n):
            if nums[i] < miniVal:
                miniVal = nums[i]
                miniIndex = i
            if nums[i] > maxVal:
                maxVal = nums[i]
                maxIndex = i
        
        left = min(miniIndex, maxIndex) + 1
        right = n - max(miniIndex, maxIndex)
        middle = abs(miniIndex - maxIndex)
        return min(left + right, left + middle, right + middle)

    def minimumDeletionsV2(self, nums: List[int]) -> int:
        n = len(nums)
        minIndex = nums.index(min(nums))
        maxIndex = nums.index(max(nums))
        
        left = min(minIndex, maxIndex) + 1
        right = n - max(minIndex, maxIndex)
        middle = abs(minIndex - maxIndex)
        
        return min(left + right, left + middle, right + middle)

        
if __name__ == "__main__":
    s = Solution()
    print(s.minimumDeletions([2,10,7,5,4,1,8,6]))  # Output: 5
    print(s.minimumDeletions([0,-4,19,1,8,-2,-3,5]))  # Output: 3
    print(s.minimumDeletions([101]))  # Output: 1
