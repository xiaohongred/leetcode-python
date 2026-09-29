class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = {}
        ans = 0
        l = 0
        for i, c in enumerate(s):
            mySet[c] = mySet.get(c, 0) + 1

            Len = i - l + 1
            while len(mySet) < Len:
                mySet[s[l]] -= 1
                if mySet[s[l]] == 0:
                    del mySet[s[l]]
                l += 1
                Len = i - l + 1
            
            ans = max(ans, Len)
        return ans

    def lengthOfLongestSubstringV2(self, s: str) -> int:
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


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring(""))
    print(s.lengthOfLongestSubstring(" "))
    print(s.lengthOfLongestSubstring("au"))
    print(s.lengthOfLongestSubstring("dvdf"))