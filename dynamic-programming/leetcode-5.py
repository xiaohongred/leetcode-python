class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < (r - l + 1):
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                    
                l -= 1
                r += 1

        return res


if __name__ == '__main__':
    s = "babad"

    solu = Solution()

    a = solu.longestPalindrome(s)
    print(a)

    s = "cbbd"
    a = solu.longestPalindrome(s)
    print(a)
