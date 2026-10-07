class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """
        根据数字键盘映射返回所有数字组合对应的字母字符串。

        例如，digits = "23" 时返回 ["ad", "ae", "af", "bd", "be",
        "bf", "cd", "ce", "cf"]。
        """
        # 数字到字母的固定映射；下标 0 和 1 不对应任何字母
        mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        n = len(digits)
        # 输入为空时没有任何组合，直接返回空列表
        if n == 0:
            return []

        # 保存所有完整的字母组合
        ans = []
        # 当前组合的每个位置；预先分配数组，避免重复追加和删除
        path = [""] * n

        def backtrack(i: int) -> None:
            """从第 i 个数字开始构造当前组合。"""
            # 递归终止条件：所有数字都已经选择完毕
            if i == n:
                ans.append("".join(path))
                return

            # 取出当前数字对应的所有候选字母
            for c in mapping[int(digits[i])]:
                # 将当前位置设为当前候选字母
                path[i] = c
                # 继续构造下一个数字
                backtrack(i + 1)
                # 下一个循环会覆盖当前位置，因此无需手动清空

        # 从第 0 个数字开始构造所有组合
        backtrack(0)
        return ans