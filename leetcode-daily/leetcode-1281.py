class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        j, h = 1, 0
        while n > 0:
            cur = n % 10
            n = n // 10
            j = j*cur
            h += cur
        return j - h


if __name__ == "__main__":
    solution = Solution()
    n = 234
    result = solution.subtractProductAndSum(n)
    print(result)  # Output: 15

    n = 4421
    result = solution.subtractProductAndSum(n)
    print(result)  # Output: 21