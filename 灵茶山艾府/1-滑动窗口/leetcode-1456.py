class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = vowel = 0
        for i, c in enumerate(s):
            if c in "aeiou":
                vowel += 1
            
            left = i - k + 1
            if left < 0:
                continue

            ans = max(ans, vowel)
            if s[left] in "aeiou":
                vowel -= 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    s = "abciiidef"
    k = 3
    result = solution.maxVowels(s, k)
    print(result)  # Output: 3

    s = "aeiou"
    k = 2
    result = solution.maxVowels(s, k)
    print(result)  # Output: 2

    s = "leetcode"
    k = 3
    result = solution.maxVowels(s, k)
    print(result)  # Output: 2

    s = "rhythms"
    k = 4
    result = solution.maxVowels(s, k)
    print(result)  # Output: 0

    s = "tryhard"
    k = 4
    result = solution.maxVowels(s, k)
    print(result)  # Output: 1