class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        pass


if __name__ == '__main__':
    s = "abcd"
    k = 2

    solu = Solution()

    a = solu.removeDuplicates(s, k)
    print(a)

    s = "deeedbbcccbdaa"
    k = 3
    a = solu.removeDuplicates(s, k)
    print(a)
