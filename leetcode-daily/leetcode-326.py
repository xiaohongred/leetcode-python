class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 3:
            n = n/3
        if n != 1:
            return False
        return True

if __name__ == "__main__":
    solution = Solution()
    n = 27
    result = solution.isPowerOfThree(n)
    print(result)  # Output: True

    n = 0
    result = solution.isPowerOfThree(n)
    print(result)  # Output: False

    n = 9
    result = solution.isPowerOfThree(n)
    print(result)  # Output: True

    n = 45
    result = solution.isPowerOfThree(n)
    print(result)  # Output: False