from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

if __name__ == "__main__":
    solution = Solution()
    arr = [0, 1, 0]
    result = solution.peakIndexInMountainArray(arr)
    print(result)  # Output: 1

    arr = [0, 2, 1, 0]
    result = solution.peakIndexInMountainArray(arr)
    print(result)  # Output: 1

    arr = [0, 10, 5, 2]
    result = solution.peakIndexInMountainArray(arr)
    print(result)  # Output: 1