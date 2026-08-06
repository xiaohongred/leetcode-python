class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # return sorted(s) == sorted(t)
        
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False

        return True


if __name__ == '__main__':
    solu = Solution()
    s = "anagram"
    t = "nagaram"
    a = solu.isAnagram(s, t)
    print(a)
