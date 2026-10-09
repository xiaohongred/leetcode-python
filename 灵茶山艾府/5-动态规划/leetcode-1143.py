from functools import cache


class Solution:
    """
    LeetCode 1143. 最长公共子序列（LCS）

    给定两个字符串 text1 和 text2，求它们的「最长公共子序列」的长度。
    子序列不要求连续，只要求字符的前后相对顺序不变，例如：
        text1 = "abcde", text2 = "ace"  ->  LCS 是 "ace"，长度为 3。

    三种写法是同一套状态的不同存储方式：
        写法一 longestCommonSubsequence        记忆化搜索   dfs(i, j)
        写法二 longestCommonSubsequenceDp      二维递推     f[i][j]
        写法三 longestCommonSubsequenceDpSaveMem  一维滚动   f[j]
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """写法一：记忆化搜索（自顶向下）。"""
        n = len(text1)
        m = len(text2)

        @cache
        def dfs(i, j):
            """
            返回：text1[0..i] 与 text2[0..j] 这两个前缀的最长公共子序列长度。

            i：text1 当前考虑到的下标（从右往左推进）
            j：text2 当前考虑到的下标（从右往左推进）
            """
            if i < 0 or j < 0:
                # 任意一边已经空掉了，公共子序列只能为空，长度为 0
                return 0
            if text1[i] == text2[j]:
                # 末尾字符相同：一定可以把它俩配上。
                # （存在一个最优解用到了这两个字符；证明的大致思路是：
                #   若某个最优解没用上 text1[i]，可以在不破坏公共性的前提下把它换进去。）
                # 配上之后，两边各退一格，长度 +1。
                return dfs(i - 1, j - 1) + 1
            # 末尾字符不同：这两个字符不可能同时出现在同一个公共子序列的末尾，
            # 于是至少有一个用不上，两种「跳过谁」的走法取较大值：
            #   跳过 text1[i] -> dfs(i-1, j)
            #   跳过 text2[j] -> dfs(i, j-1)
            return max(dfs(i - 1, j), dfs(i, j - 1))

        return dfs(n - 1, m - 1)

    def longestCommonSubsequenceDp(self, text1: str, text2: str) -> int:
        """
        写法二：二维表递推（自底向上）。

        与写法一的对应关系：f[i][j] <==> dfs(i - 1, j - 1)。
        （dfs 的下标从 0 开始、可以为 -1；表里多补了一行一列专门表示「空前缀」。）
        """
        n = len(text1)
        m = len(text2)

        # f[i][j]：text1 的前 i 个字符（text1[0..i-1]）与 text2 的前 j 个字符
        #          （text2[0..j-1]）的最长公共子序列长度。
        # 下标 0 表示「空串」，所以表格是 (n+1) 行 × (m+1) 列，
        # 第 0 行、第 0 列全部为 0（任一串为空时 LCS 长度都是 0）——
        # 这正是写法一里 `i < 0 or j < 0: return 0` 那个边界。
        f = [[0] * (m + 1) for _ in range(n + 1)]

        for i, x in enumerate(text1):        # x = text1[i]，对应表里的第 i+1 行
            for j, y in enumerate(text2):    # y = text2[j]，对应表里的第 j+1 列
                if x == y:
                    # 两个末尾字符相同：直接接在「各去掉一个字符」的答案后面
                    f[i + 1][j + 1] = f[i][j] + 1
                    # 这里不需要再和 max(f[i+1][j], f[i][j+1]) 比较，并不是漏写：
                    # 给任意一个字符串多加一个字符，LCS 长度最多只能 +1，所以
                    #     f[i][j+1] <= f[i][j] + 1 且 f[i+1][j] <= f[i][j] + 1
                    # 也就是说 f[i][j] + 1 已经不比它们任何一个小了，取 max 是多余的。
                else:
                    # 末尾字符不同：至少有一个用不上，于是「跳过 text1[i]」与
                    # 「跳过 text2[j]」两种走法取较大值。
                    #   f[i][j+1] -> 沿用「没算 text1[i]」的答案（跳过 x）
                    #   f[i+1][j] -> 沿用「没算 text2[j]」的答案（跳过 y）
                    f[i + 1][j + 1] = max(f[i + 1][j], f[i][j + 1])

        return f[n][m]

    def longestCommonSubsequenceDpSaveMem(self, text1: str, text2: str) -> int:
        """
        写法三：一维数组滚动（在写法二的基础上压掉 text1 那一维）。

        算 f[i+1][*] 只用得到 f[i][*] 和 f[i+1][*]（同一行），所以可以把整张表压成
        一个长度 m+1 的数组，逐行覆盖。但「覆盖」会带来一个麻烦：
        f[i+1][j+1] 需要读左上方那一格 f[i][j]，而它接下来就会被本行写坏，
        所以要用一个变量把它先存下来 —— 这就是下面 prev 的作用。
        """
        n = len(text1)
        m = len(text2)

        # f[j] 在每轮外层循环（处理 text1[i]）中滚动表示：
        #   * 进入本轮之前：f[j] = f[i][j]     （text1 前 i 个字符 与 text2 前 j 个）
        #   * 本轮结束之后：f[j] = f[i+1][j]   （多算了 text1[i]）
        # 初始 f 全是 0，正好对应表格第 0 行（text1 为空）。
        f = [0] * (m + 1)

        for i, x in enumerate(text1):        # x = text1[i]
            prev = 0                         # prev 代表「左上角」f[i][j]；
                                             # j = 0 时，f[i][0] = 0（text2 为空）
            for j, y in enumerate(text2):    # y = text2[j]
                temp = f[j + 1]              # 先存下旧的 f[j+1]，它就是 f[i][j+1]

                if x == y:
                    # 左上角 + 1（左上角的旧值一直由 prev 保管着）
                    f[j + 1] = prev + 1
                else:
                    #   f[j]     —— 本行刚更新过，是 f[i+1][j]，「跳过 x」的答案
                    #   f[j+1]   —— 还没更新，是 f[i][j+1]，「跳过 y」的答案
                    f[j + 1] = max(f[j + 1], f[j])

                # 本列算完，下一列的「左上角」就是本列被覆盖前的旧值 f[i][j+1]
                prev = temp
            # 一行处理完，f[j] 全部变成 f[i+1][j]

        return f[m]                          # 即 f[n][m]


if __name__ == "__main__":
    # 三种写法答案一致，写法三只是省掉了 text1 那一维空间
    s = Solution()
    print(s.longestCommonSubsequence("abcde", "ace"))  # 3
    print(s.longestCommonSubsequence("abc", "abc"))    # 3
    print(s.longestCommonSubsequence("abc", "def"))    # 0
    print(s.longestCommonSubsequenceDp("abcde", "ace"))  # 3
    print(s.longestCommonSubsequenceDp("abc", "abc"))    # 3
    print(s.longestCommonSubsequenceDp("abc", "def"))    # 0