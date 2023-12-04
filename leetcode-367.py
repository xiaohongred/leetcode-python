class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l, r = 0, num // 2

        while l <= r:
            mid = (r - l) // 2 + l
            mm = mid * mid
            if mm < num:
                l = mid + 1
            elif mm > num:
                r = mid - 1
            else:
                return True

        return False


if __name__ == '__main__':
    num = 16
    s = Solution()
    a = s.isPerfectSquare(num)
    b = s.isPerfectSquare(1)
    c = s.isPerfectSquare(12)
    print(a)
    print(b)
    print(c)
