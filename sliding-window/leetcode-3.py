class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


if __name__ == '__main__':
    solu = Solution()
    s = "abcabcbb"
    a = solu.lengthOfLongestSubstring(s)
    print(a)

    s = "bbbbb"
    a = solu.lengthOfLongestSubstring(s)
    print(a)

    s = "pwwkew"
    a = solu.lengthOfLongestSubstring(s)
    print(a)
