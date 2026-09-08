class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        count = 0
        for i in range(1000, n + 1):
            if i // 1000 > 0:
                count += 1

            if i // 1000000 > 0:
                count += 1
        return count

    def countCommasV2(self, n: int) -> int:
        if n < 1000:
            return 0
        count = n - 1000 + 1
        
        return count

        

if __name__ == "__main__":
    solution = Solution()
    n = 1002
    result = solution.countCommas(n)
    print(result)  # Output: 3

    n = 998
    result = solution.countCommas(n)
    print(result)  # Output: 0

    n = 1002
    result = solution.countCommasV2(n)
    print(result)  # Output: 3

    n = 998
    result = solution.countCommasV2(n)
    print(result)  # Output: 0