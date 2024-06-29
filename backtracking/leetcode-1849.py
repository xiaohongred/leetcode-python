class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(index, prev):
            if index == len(s):
                return True
            for j in range(index, len(s)):
                val = int(s[index:j + 1])
                if val + 1 == prev and dfs(j + 1, val):
                    return True
            return False

        for i in range(len(s) - 1):  # 至少要将s拆成2部分
            val = int(s[:i + 1])  # s[0:i+1] 第一个数
            if dfs(i + 1, val):
                return True
        return False


if __name__ == '__main__':
    s = "050043"
    solu = Solution()
    a = solu.splitString(s)
    print(a)
