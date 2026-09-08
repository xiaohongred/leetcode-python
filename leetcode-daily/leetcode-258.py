class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            res = 0  # 每轮求和前清空，避免累加出错
            while num > 0:
                cur = num % 10
                num = num // 10
                res += cur
            num = res
        return num

    def addDigitsV2(self, num: int) -> int:
        res = 0
        while True:
            while num > 0:
                cur = num % 10
                num = num // 10
                res += cur
            
            num = res
            res = 0
            if num < 10:
                break
        return num

if __name__ == "__main__":
    solution = Solution()
    num = 38
    result = solution.addDigits(num)
    print(result)  # Output: 2

    num = 0
    result = solution.addDigits(num)
    print(result)  # Output: 0


    num = 38
    result = solution.addDigitsV2(num)
    print(result)  # Output: 2

    num = 0
    result = solution.addDigitsV2(num)
    print(result)  # Output: 0