class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        for i in range(n):
            maxI = max(nums[0:i+1])

            minI = min(nums[i:n])

            if maxI - minI <= k:
                return i
        return -1


if __name__ == "__main__":
    nums = [5,0,1,4]
    k = 3
    solution = Solution()
    result = solution.firstStableIndex(nums, k)
    print(result)  # Output: 3


    nums = [3,2,1]
    k = 1
    result = solution.firstStableIndex(nums, k)
    print(result)  # Output: -1


    nums = [0]
    k = 0
    result = solution.firstStableIndex(nums, k)
    print(result)  # Output: 0