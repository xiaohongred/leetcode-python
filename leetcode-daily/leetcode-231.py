class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        
        while n >= 2:
            n = n / 2
        
        if n != 1:
            return False
        return True

if __name__ == "__main__":
    solution = Solution()
    n = 1
    result = solution.isPowerOfTwo(n)
    print(result)  # Output: True

    n = 16
    result = solution.isPowerOfTwo(n)
    print(result)  # Output: True

    n = 3
    result = solution.isPowerOfTwo(n)
    print(result)  # Output: False