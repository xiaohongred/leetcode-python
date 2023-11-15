class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()

        nnStr = newStr[::-1]
        return nnStr == newStr

    def isPalindromeV2(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1

            while r > l and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True


if __name__ == '__main__':
    s = Solution()
    myStr = "A man, a plan, a canal: Panama"
    a = s.isPalindrome(myStr)
    print(a)

    b = s.isPalindromeV2(myStr)
    print(b)

    print(ord('A'), ord('a'))
    print(ord('0'), ord('9'))
