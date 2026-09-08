from typing import List
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = set('aeiou')
        count = 0
        for i in range(left, right + 1):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                count += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    words = ["are","amy","u"]
    left = 0
    right = 2
    result = solution.vowelStrings(words, left, right)
    print(result)  # Output: 2

    words = ["hey","aeo","mu","ooo","artro"]
    left = 1
    right = 4
    result = solution.vowelStrings(words, left, right)
    print(result)  # Output: 3