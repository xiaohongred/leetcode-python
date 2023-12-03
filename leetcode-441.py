class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0
        while l <= r:
            mid = (r - l) // 2 + l
            coins = (mid / 2) * (1 + mid)
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(mid, res)
        return res


if __name__ == '__main__':
    pass
