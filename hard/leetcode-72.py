class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)

        # equal -->  (i+1, j+1)
        # insert --> (i, j+1)
        # delete --> (i+1, j)
        # replace -> (i+1, j+1)
        cache = {}

        def dfs(i, j):  # 返回 从 word1[i] word[j] 开始最少需要做多少次操作
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(word1) and j >= len(word2):
                return 0
            if i >= len(word1):
                return len(word2) - j  # 需要往 word1 后面 insert 这么多次
            if j >= len(word2):
                return len(word1) - i  # 需要删掉 word1 后面 (len(word1) - i)个 字母
            if word1[i] == word2[j]:  # 相等，当前位置不需要操作
                res = dfs(i + 1, j + 1)
                cache[(i, j)] = res
                return res
            res1 = dfs(i, j + 1)  # insert
            res2 = dfs(i + 1, j)  # delete
            res3 = dfs(i + 1, j + 1)  # replace

            finalRes = min(res1, res2, res3) + 1
            cache[(i, j)] = finalRes
            return finalRes

        return dfs(0, 0)


if __name__ == '__main__':
    s = Solution()
    word1 = "horse"
    word2 = "ros"
    a = s.minDistance(word1, word2)
    print(a)

    word1 = "intention"
    word2 = "execution"
    a = s.minDistance(word1, word2)
    print(a)
