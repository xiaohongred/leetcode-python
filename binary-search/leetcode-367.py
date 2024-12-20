class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num + 1):
            if i * i == num:
                return True
            if i * i > num:
                return False

    def isPerfectSquareV2(self, num: int) -> bool:
        l, r = 1, num
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                l = mid + 1
            elif mid * mid > num:
                r = mid - 1
        return False


if __name__ == '__main__':
    s = Solution()
    num = 16
    a = s.isPerfectSquare(num)
    print(a)

    num = 14
    a = s.isPerfectSquare(num)
    print(a)

    num = 16
    a = s.isPerfectSquareV2(num)
    print(a)

    num = 14
    a = s.isPerfectSquareV2(num)
    print(a)
