class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        alt1, alt2 = "", ""
        for i in range(len(s)):
            alt1 += "0" if i % 2 else "1"
            alt2 += "1" if i % 2 else "0"

        res = len(s)
        diff1, diff2 = 0, 0
        l = 0
        for r in range(len(s)):
            if s[r] != alt1[r]:
                diff1 += 1
            if s[r] != alt2[r]:
                diff2 += 1
            if (r - l + 1) > n:  # 窗口长度大于n, l 可以右移了
                if s[l] != alt1[l]:
                    diff1 -= 1
                if s[l] != alt2[l]:
                    diff2 -= 1
                l += 1
            if (r - l + 1) == n:  # 窗口长度等于n,判断当前的diff个数是否为最小
                res = min(res, diff1, diff2)
        return res


if __name__ == '__main__':
    solu = Solution()
    s = "111000"
    a = solu.minFlips(s)
    print(a)

    s = "010"
    a = solu.minFlips(s)
    print(a)

    s = "1110"
    a = solu.minFlips(s)
    print(a)
