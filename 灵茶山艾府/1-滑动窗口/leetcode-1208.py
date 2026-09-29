class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # 滑动窗口：窗口内 |s[i]-t[i]| 之和 <= maxCost
        ans = 0
        left = 0
        cost = 0
        for right in range(len(s)):
            cost += abs(ord(s[right]) - ord(t[right]))
            while cost > maxCost:                 # 超预算，收缩左边界
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, right - left + 1)
        return ans

    def equalSubstringV2(self, s: str, t: str, maxCost: int) -> int:
        # 前缀和 + 二分：每个左端点找最远的右端点
        n = len(s)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + abs(ord(s[i]) - ord(t[i]))
        ans = 0
        for left in range(n):
            # 找最大的 right，使得 pre[right+1] - pre[left] <= maxCost
            lo, hi = left, n
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if pre[mid] - pre[left] <= maxCost:
                    lo = mid
                else:
                    hi = mid - 1
            ans = max(ans, lo - left)
        return ans


if __name__ == "__main__":
    sol = Solution()
    cases = [
        ("abcd", "bcdf", 3, 3),
        ("abcd", "cdef", 3, 1),
        ("abcd", "acde", 0, 1),
        ("abcd", "bcdf", 0, 0),
        ("abcdef", "abcdef", 100, 6),
        ("a", "z", 25, 1),
        ("a", "z", 24, 0),
    ]
    for s, t, maxCost, expected in cases:
        got1 = sol.equalSubstring(s, t, maxCost)
        got2 = sol.equalSubstringV2(s, t, maxCost)
        print(f"{s!r} -> {t!r}, {maxCost}: {got1}, {got2} (expected {expected})",
              "OK" if got1 == got2 == expected else "FAIL")
