from builtins import str


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        calcIndex = [0, 0]
        sLen = len(s)
        index = sLen - 1
        while index >= 0 and s[index] == ' ':
            index -= 1

        calcIndex[0] = index

        while index >= 0 and s[index] != ' ':
            index -= 1

        calcIndex[1] = index

        return calcIndex[0] - calcIndex[1]


if __name__ == '__main__':
    s = Solution()
    str = "Hello World"
    a = s.lengthOfLastWord(str)
    print(a)
