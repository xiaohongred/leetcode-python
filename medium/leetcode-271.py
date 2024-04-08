# https://www.lintcode.com/problem/659/

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        # write your code here
        res = []
        i = 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            s = str[j + 1:j + 1 + length]
            res.append(s)

            i = j + 1 + length
        return res


if __name__ == '__main__':
    s = Solution()
    strList = ["lint", "code", "love", "you"]
    print(strList)
    str = s.encode(strList)
    print(str)
    a = s.decode(str)
    print(a)
