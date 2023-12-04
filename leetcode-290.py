class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False

        charToWord = {}
        wordToChar = {}
        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False

            charToWord[c] = w
            wordToChar[w] = c

        return True


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    so = Solution()
    a = so.wordPattern(pattern, s)
    print(a)
