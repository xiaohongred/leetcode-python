from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        total = 0
        for i, n in enumerate(arr):
            left = i - k + 1
            total += n

            if left < 0:
                continue
            
            avg = total*1.0/k
            if avg >= threshold:
                ans += 1
            total -= arr[left]
        return ans


if __name__ == "__main__":
    solution = Solution()
    arr = [2,2,2,2,5,5,5,8]
    k = 3
    threshold = 4
    result = solution.numOfSubarrays(arr, k, threshold)
    print(result)  # Output: 3

    arr = [1,1,1,1,1]
    k = 1
    threshold = 0
    result = solution.numOfSubarrays(arr, k, threshold)
    print(result)  # Output: 5

    arr = [11,13,17,23,29,31,7,5,2,3]
    k = 3
    threshold = 5
    result = solution.numOfSubarrays(arr, k, threshold)
    print(result)  # Output: 6

    arr = [7,7,7,7,7]
    k = 5
    threshold = 7
    result = solution.numOfSubarrays(arr, k, threshold)
    print(result)  # Output: 1

    arr = [4,4,4,4]
    k = 4
    threshold = 1
    result = solution.numOfSubarrays(arr, k, threshold)
    print(result)  # Output: 1