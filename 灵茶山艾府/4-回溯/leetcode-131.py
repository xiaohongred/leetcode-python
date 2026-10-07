class Solution:
    def partition(self, s: str) -> list[list[str]]:
        """
        将字符串 s 切分为多个回文串，并返回所有切分方案。

        例如，s = "aab" 时返回 [
            ["a", "a", "b"],
            ["aa", "b"],
        ]。
        """
        # 保存所有完整的回文串切分方案
        ans = []
        # 当前正在构建的切分路径
        path = []

        n = len(s)

        def dfs(i: int) -> None:
            """从下标 i 开始切分字符串 s。"""
            # 递归终止条件：所有字符已经被切分
            if i == n:
                # 复制路径，避免后续回滚后已保存结果被修改
                ans.append(path.copy())
                return

            # 从 i 到 n-1 依次尝试当前子串的结束位置
            for j in range(i, n):
                # 取出从 i 到 j 的子串
                t = s[i: j + 1]

                # 只有回文串才加入当前路径
                if t == t[::-1]:
                    path.append(t)
                    # 继续从当前子串之后开始切分
                    dfs(j + 1)
                    # 回滚：移除刚加入的子串，恢复路径状态
                    path.pop()

        # 从字符串开头开始搜索所有回文串切分方案
        dfs(0)
        return ans


if __name__ == "__main__":
    s = Solution()
    input_str = "aab"
    result = s.partition(input_str)
    print(result)  # 输出所有回文分割方案