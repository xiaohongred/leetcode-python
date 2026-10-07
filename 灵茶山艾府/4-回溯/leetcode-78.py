class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        使用“选择或不选择”分支生成 nums 的所有子集。

        每个元素都有两种决策：不加入当前路径，或加入当前路径。
        """
        # 保存所有完整的子集
        ans = []
        # 当前正在构建的子集
        path = []
        n = len(nums)

        def dfs(i: int) -> None:
            """从 nums 的下标 i 开始构造子集。"""
            # 递归终止条件：所有元素都已经处理完毕
            if i == n:
                # 复制路径，避免后续递归修改已保存的结果
                ans.append(path.copy())
                return

            # 分支一：不选择 nums[i]，继续处理下一个元素
            dfs(i + 1)

            # 分支二：选择 nums[i]，把它加入当前路径
            path.append(nums[i])
            dfs(i + 1)
            # 回滚：移除刚加入的元素，恢复到“不选择”分支的状态
            path.pop()

        # 从 nums 的第 0 个元素开始生成所有子集
        dfs(0)
        return ans

    def subsetsV2(self, nums: list[int]) -> list[list[int]]:
        """
        使用“从当前下标开始选择连续范围”生成所有子集。

        该版本在进入 dfs 时就保存当前路径，通过 j 逐个选择当前
        剩余元素，从而避免重复生成相同的组合。
        """
        # 保存所有完整的子集
        ans = []
        # 当前正在构建的子集
        path = []
        n = len(nums)

        def dfs(i: int) -> None:
            """从 nums 的下标 i 开始选择元素。"""
            # 保存当前路径；这也会记录空子集
            ans.append(path.copy())

            # 所有元素都已经被考虑完毕
            if i == n:
                return

            # 从 i 到 n-1 依次选择当前剩余元素
            for j in range(i, n):
                path.append(nums[j])
                # 之后只从 j+1 开始选择，避免重复选中同一个元素
                dfs(j + 1)
                # 回滚：移除当前选择，准备下一个候选元素
                path.pop()

        # 从 nums 的第 0 个元素开始生成所有子集
        dfs(0)
        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    result = s.subsets(nums)
    print(result)  # 输出所有子集