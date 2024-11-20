class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pass


if __name__ == '__main__':
    solu = Solution()

    s = "ADOBECODEBANC"
    t = "ABC"
    a = solu.minWindow(s, t)
    print(a)

    s = "a"
    t = "a"
    a = solu.minWindow(s, t)
    print(a)

    s = "a"
    t = "aa"
    a = solu.minWindow(s, t)
    print(a)
