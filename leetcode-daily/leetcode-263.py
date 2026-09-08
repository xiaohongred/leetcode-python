class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        for p in[2,3,5]:
            while n%p==0:
                n//=p
        return n==1


if __name__ == "__main__":
    solution = Solution()
    n = 6
    result = solution.isUgly(n)
    print(result)  # Output: True

    n = 1
    result = solution.isUgly(n)
    print(result)  # Output: True

    n = 14
    result = solution.isUgly(n)
    print(result)  # Output: False