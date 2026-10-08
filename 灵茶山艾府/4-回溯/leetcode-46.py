from typing import List


class Solution:
    """
    LeetCode 46. 全排列

    给定一个不含重复数字的数组 nums，返回其所有可能的全排列。
    例如 nums = [1, 2, 3] 时共有 n! = 6 种排列。

    下面给出两种经典写法，本质都是「按位置从左到右填数」的回溯，
    区别只在于「如何表示自己还有哪些数可以用」：

      * permute   —— 显式携带一个集合 s，表示「剩余可选的数」，
                     每层把新集合 s - {x} 传给下一层。
      * permuteV2 —— 原地交换：把选中的数换到下标 start 处，
                     递归返回后再换回来（手动恢复现场）。

    时间复杂度都是 O(n! · n)：共 n! 个叶子结点，每个叶子要拷贝一份长度 n 的答案
    （即下面 `path.copy()` / `nums[:]` 带来的那个额外的 n）。
    """

    def permute(self, nums: list[int]) -> list[list[int]]:
        """写法一：位置型回溯 + 用集合记录「还没用过的数」。"""
        n = len(nums)
        ans = []

        # path[i] 表示排列中第 i 个位置上最终填的数字。
        # 长度固定为 n，用「下标赋值」覆盖写入，而不是 append / pop。
        path = [0] * n

        def dfs(i, s):
            """
            i：下一个要填的位置下标（即前 i 个位置已经填好了）
            s：还没有被用过的数字集合，也就是「本层及之后还能挑的数」

            决策：位置 i 上放哪个数？只能从剩余集合 s 里挑一个。
            """
            # 终点：n 个位置全部填满，此时 path 就是一个完整的排列
            if i == n:
                # 必须 copy！
                # path 全程复用同一个列表对象，若直接 append(path)，存进 ans 的是
                # 「引用」，之后会被别的分支覆盖，最终 ans 里会变成 n! 份相同内容
                # （都是最后一次搜索剩下的结果）。
                ans.append(path.copy())
                return

            # 枚举「位置 i 放哪个数」——候选就是 s 里的每一个数
            for x in s:
                path[i] = x  # 做选择：把 x 放到位置 i
                # 进入下一层：x 已经被用掉，所以可选集合要变成 s - {x}。
                # 注意 s - {x} 是「新建」的集合，并没有原地修改 s。
                dfs(i + 1, s - {x})
                # 这里不需要显式「撤销选择 / 恢复现场」，原因有两点：
                #   1) path[i] 会在同一层的下一次循环里被直接覆盖，不会残留；
                #   2) s 在本层从头到尾都没被改动，"去掉 x" 是通过把新集合传给
                #      下一层完成的，所以兄弟分支看到的 s 完全一样。
                # 这就是「不可变思路」带来的便利：天然免去回溯恢复这一步。

        dfs(0, set(nums))  # 从位置 0 开始，此时所有数字都还没用过
        return ans

    def permuteV2(self, nums: List[int]) -> List[List[int]]:
        """写法二：原地交换，不需要额外的 used 数组或集合。"""
        n = len(nums)
        res: List[List[int]] = []

        def backtrack(start: int) -> None:
            """
            start：还没确定的位置区间的左端点。
                   此刻 nums[0 .. start-1] 已经确定好（就是答案的前 start 项），
                   而「所有还没被用过的数」恰好都留在 nums[start .. n-1] 里。

            决策：下标 start 位置上放谁？就从 nums[start .. n-1] 中任选一个，
                  把它交换到 start 处，它就被固定下来了。
            """
            # 终点：所有位置都确定了，当前的 nums 就是一种排列
            if start == n:
                # 同样必须拷贝！nums 全程是同一个列表，不拷贝就会存成引用，
                # 之后被交换操作改写，最终 res 里全是同一个数组。
                res.append(nums[:])
                return

            # 枚举「把谁换到 start 位置」：i 从 start 一路取到 n-1
            for i in range(start, n):
                # 交换：让 nums[i] 顶替到 start 位置（做选择）
                nums[start], nums[i] = nums[i], nums[start]
                # 位置 start 已经确定，递归去确定 start + 1
                backtrack(start + 1)
                # 撤销选择：换回原样，否则会污染同一层的其它兄弟分支。
                # 这里的 i 是本层的循环变量，递归过程中不会被改变，所以能精确换回。
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res
    def permuteV3(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []
        path = [0] * n
        on_path = [False] * n
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return  
            for j in range(n):
                if on_path[j]:
                    continue
                path[i] = nums[j]
                on_path[j] = True
                dfs(i + 1)
                on_path[j] = False
        dfs(0)
        return ans

if __name__ == "__main__":
    s = Solution()
    # 两种写法返回的是同一组排列，但「顺序」不保证相同：
    # 写法一用 set 迭代，顺序由元素哈希决定，既不按输入顺序也不保证字典序。
    print(s.permute([1, 2, 3]))
    print(s.permuteV2([1, 2, 3]))


# =============================================================================
# 两种写法对比小结
# =============================================================================
#
# 1) 共同点：都是「按位置填数」的回溯。
#    第 i 层决定下标 i 放哪个数，走到 i == n 就产出一个答案。
#
# 2) 差异：如何表示「还没用过的数」
#    - permute  ：显式携带集合 s，把「新状态」s - {x} 传给下一层。
#                 好处：不修改任何共享状态，不需要恢复现场，出错点少；
#                 代价：每层都要新建集合，有额外的空间与拷贝开销。
#    - permuteV2：把「还没用过的数」隐含在下标区间 [start, n) 里，
#                 通过交换把选中的数换到 start 处。
#                 好处：不需要额外的 used / 集合，额外空间只有递归栈；
#                 代价：原地修改了输入数组，必须手动换回来，
#                       一旦漏掉恢复这一步，兄弟分支的结果就会被污染。
#                （本函数退出时会全部换回原样，所以调用方看到的 nums 并未改变。）
#
# 3) 两者都假设 nums 中没有重复数字。
#    若允许重复（LeetCode 47. 全排列 II），需要先排序 + 在同一层去重，
#    否则会产出重复的排列。