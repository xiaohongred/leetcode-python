class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0
        while l <= r:
            mid = (r - l) // 2 + l
            coins = (mid * (1 + mid)) / 2
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(mid, res)
        return res


if __name__ == '__main__':
    s = Solution()

    n = 8
    a = s.arrangeCoins(n)
    print(a)

    n = 5
    a = s.arrangeCoins(n)
    print(a)
