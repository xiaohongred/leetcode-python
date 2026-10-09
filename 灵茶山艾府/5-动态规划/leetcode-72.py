from functools import cache


class Solution:
    """
    LeetCode 72. 编辑距离

    给定两个单词 word1 和 word2，每次可以「插入、删除、替换」任意一个字符，
    求把 word1 变成 word2 所需的「最少操作次数」。

    三种写法是同一套状态的不同存储方式：
        写法一 minDistance              记忆化搜索    dfs(i, j)
        写法二 minDistanceDp            二维递推      f[i][j]
        写法三 minDistanceDpSaveMem     一维滚动      f[j]
    """

    def minDistance(self, word1: str, word2: str) -> int:
        """写法一：记忆化搜索（自顶向下）。"""
        n = len(word1)
        m = len(word2)

        @cache
        def dfs(i, j):
            """
            返回：把 word1[0..i] 变成 word2[0..j] 所需的最少操作次数。

            i：word1 当前考虑到的下标（从右往左推进）
            j：word2 当前考虑到的下标（从右往左推进）
            """
            if i < 0:
                # word1 已经空了：只能往里插入 word2 的全部 j+1 个字符
                return j + 1
            if j < 0:
                # word2 已经空了：只能把 word1 剩下的 i+1 个字符全删掉
                return i + 1

            if word1[i] == word2[j]:
                # 末尾字符相同，直接让这两个字符配对，一步都不用花
                # （为什么一定可以不花代价？见写法二里那段说明）
                return dfs(i - 1, j - 1)
            else:
                # 末尾字符不同，三种操作任选其一，取代价最小的，操作本身还要 +1：
                #   删除：删掉 word1[i]              -> dfs(i-1, j)
                #   插入：在 word1 末尾补上 word2[j] -> dfs(i, j-1)
                #   替换：把 word1[i] 改成 word2[j]  -> dfs(i-1, j-1)
                return min(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1)) + 1

        return dfs(n - 1, m - 1)

    def minDistanceDp(self, word1: str, word2: str) -> int:
        """
        写法二：二维表递推（自底向上）。

        与写法一的对应关系：f[i][j] <==> dfs(i - 1, j - 1)。
        （dfs 的下标可以到 -1，表里多补一行一列专门表示「空串」。）
        """
        n = len(word1)
        m = len(word2)

        # f[i][j]：把 word1 的前 i 个字符（word1[0..i-1]）变成
        #          word2 的前 j 个字符（word2[0..j-1]）所需的最少操作次数。
        f = [[0] * (m + 1) for _ in range(n + 1)]
        # 边界：word1 为空，要变成 word2 的前 j 个字符，只能插入 j 次
        f[0] = list(range(m + 1))

        for i, x in enumerate(word1):        # x = word1[i]，对应表格第 i+1 行
            # 边界：word2 为空，只能把 word1 的前 i+1 个字符全部删掉
            f[i + 1][0] = i + 1
            for j, y in enumerate(word2):    # y = word2[j]，对应表格第 j+1 列
                if x == y:
                    f[i + 1][j + 1] = f[i][j]
                    # 这里不需要再和另外两条路径取 min，并不是漏写：
                    # 给任意一个字符串加上/去掉一个字符，编辑距离最多变化 1，所以
                    #     f[i+1][j] + 1 >= f[i][j]   且   f[i][j+1] + 1 >= f[i][j]
                    # 即「直接配对」这条路的代价已经是最小的了。
                else:
                    # 三种操作取最小，再加上本次操作本身的 1 步：
                    #   f[i + 1][j]  -> 插入：先让 word1 前 i+1 个字符变到 word2 前 j 个，
                    #                          再补上 word2[j]
                    #   f[i][j + 1]  -> 删除：先变出 word2 前 j+1 个字符，再删掉 word1[i]
                    #   f[i][j]      -> 替换：前 i-1 / j-1 个字符弄好后，把 word1[i] 换成 word2[j]
                    f[i + 1][j + 1] = min(f[i + 1][j], f[i][j + 1], f[i][j]) + 1

        return f[n][m]

    def minDistanceDpSaveMem(self, word1: str, word2: str) -> int:
        """
        写法三：一维数组滚动（在写法二的基础上压掉 word1 那一维）。

        算 f[i+1][*] 只用得到 f[i][*]（上一行）和 f[i+1][*]（本行已经算好的部分），
        所以整张表可以压成一个长度 m+1 的数组、逐行覆盖。
        但覆盖会带来一个麻烦：f[i+1][j+1] 要用到左上角那一格 f[i][j]，
        而那一格马上就要被本行写坏，所以必须先用一个变量把它存住
        —— 这就是下面 prev 的作用（和 1143 题 LCS 里用的是同一个套路）。

        空间由 O(n · m) 降到 O(m)。
        """
        n = len(word1)
        m = len(word2)

        # f[j] 随外层循环滚动表示：
        #   * 进入本轮之前：f[j] = f[i][j]    （word1 前 i 个字符 -> word2 前 j 个字符）
        #   * 本轮结束之后：f[j] = f[i+1][j]  （多考虑了字符 word1[i]）
        # 初值 list(range(m + 1)) 正好就是边界 f[0][j] = j（word1 为空，只能插入 j 次）。
        f = list(range(m + 1))

        for i, x in enumerate(word1):        # x = word1[i]
            prev = f[0]                      # 先把 f[i][0] 存下来，它就是 (i, 0) 的「左上角」
            f[0] = i + 1                     # 边界：f[i+1][0] = i+1（word2 为空，删 i+1 次）

            for j, y in enumerate(word2):    # y = word2[j]
                temp = f[j + 1]              # 先存下旧的 f[j+1]，也就是正上方的 f[i][j+1]

                if x == y:
                    f[j + 1] = prev          # 直接配对，代价等于左上角 f[i][j]
                else:
                    # 三个候选依次是「删 / 插 / 换」，注意它们各自的来源：
                    #   f[j + 1] —— 本行还没写过，仍是 f[i][j+1]（正上方，删除）
                    #   f[j]     —— 本行刚更新过，已是 f[i+1][j]（左方，插入）
                    #   prev     —— 左上角 f[i][j]（替换）
                    f[j + 1] = min(f[j + 1], f[j], prev) + 1

                prev = temp                  # 本列用完，下一列的「左上角」就是本列被覆盖前的旧值
            # 一行处理完，f[j] 全部变成 f[i+1][j]

        return f[m]                          # 即 f[n][m]


if __name__ == "__main__":
    # 三种写法答案一致，写法三只是省掉了 word1 那一维空间
    s = Solution()
    print(s.minDistance("horse", "ros"))  # 3
    print(s.minDistance("intention", "execution"))  # 5