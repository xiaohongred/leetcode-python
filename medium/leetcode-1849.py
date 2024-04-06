class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(index, prevVal):
            if index == len(s):
                return True
            for j in range(index, len(s)):
                val = int(s[index: j + 1])
                if prevVal - val == 1 and dfs(j + 1, val):
                    return True
            return False

        for i in range(len(s) - 1):
            val = int(s[:i + 1])  # s[: i + 1] 左闭右开
            if dfs(i + 1, val):
                return True
        return False


if __name__ == '__main__':
    s = "1234"
    solu = Solution()
    a = solu.splitString(s)
    print(a)

    s = "4321"
    a = solu.splitString(s)
    print(a)
