class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

    def characterReplacementV2(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxF = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])
            while (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1  # l 右移时不需要更新（减小）maxF, 因为 res 只有在发现大的 maxF 时才更新
            res = max(res, r - l + 1)
        return res


if __name__ == '__main__':
    solu = Solution()
    s = "ABAB"
    k = 2
    a = solu.characterReplacement(s, k)
    print(a)

    s = "AABABBA"
    k = 1
    a = solu.characterReplacement(s, k)
    print(a)
