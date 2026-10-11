from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    LeetCode 124. 二叉树中的最大路径和

    路径被定义为「沿父子边连接起来的一条节点序列」，同一个节点最多出现一次；
    路径不必经过根，也不必从上往下（可以在某个节点处「拐弯」）。
    求所有路径的节点值之和的最大值。
    例如 [1,2,3] -> 6（2 -> 1 -> 3），[-10,9,20,null,null,15,7] -> 42（15 -> 20 -> 7）。

    ── 两个必须分清的量 ────────────────────────────────────────────────
    这是本题最关键的地方，先记住结论：
        * dfs(node) 的【返回值】：以 node 为起点、只朝【一侧】往下延伸的一条链
                                  的最大和；如果是负的就返回 0（表示宁可不要这条链）。
                                  它是个「还要往父节点传」的半成品。
        * 全局 ans：【真正的答案】。它允许路径在某个节点处拐弯，也就是
                                  l_val + r_val + node.val（左边 + 自己 + 右边）。
                                  拐过弯的路径没法再往父节点接，所以它只能进答案，
                                  不能作为返回值。

    一句话：**返回值只能带一条腿往上走，答案可以在原地劈个叉。**

    ── 为什么返回值是 max(max(l, r) + node.val, 0) ─────────────────────
        * 只取 max(l, r)：往上走时路径不能分叉，父节点只能接住一侧；
        * 再和 0 取 max：若这条链总和为负，它对上层只会是拖累，不如「不接」——
          用 0 表示「这一侧不用」。于是上层拿到的 l_val / r_val 永远 >= 0。
    """

    def maxPathSum(self, root: TreeNode | None) -> int:
        # 答案可能全是负数（比如每个节点都是负数的树），所以初值用 -inf 而不是 0。
        # 若写 0，相当于允许「空路径」，在全负的树上会错误地返回 0。
        ans = float('-inf')

        def dfs(node):
            """后序遍历：先算左右子树，再处理当前节点。"""
            if node is None:
                # 空节点贡献 0，等价于「这一侧没有链可用」
                return 0

            # 先递归左右子树，取回「左/右子树能向上提供的最佳单侧链」。
            # 因为下面 return 时和 0 取过 max，这两个值一定 >= 0。
            l_val = dfs(node.left)
            r_val = dfs(node.right)

            nonlocal ans
            # 在 node 处「拐弯」的路径：左链 + node + 右链，拿去更新全局答案。
            # 这一行不需要任何额外分支，因为它天然覆盖了全部四种形态：
            #     左右都用 -> l_val > 0 且 r_val > 0
            #     只用左边 -> r_val 被 0 顶掉
            #     只用右边 -> l_val 被 0 顶掉
            #     只用自己 -> l_val、r_val 都被 0 顶掉
            # 这正是「负链归零」带来的好处。
            ans = max(ans, l_val + r_val + node.val)

            # 返回值：只能带一条腿往上走，所以左右里挑大的，再加自己；
            # 若整条链是负的，就返回 0（等于告诉父节点：别接我这一侧）。
            return max(max(l_val, r_val) + node.val, 0)

        dfs(root)
        return ans


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    print(s.maxPathSum(root))  # 6
    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(s.maxPathSum(root))  # 42


# =============================================================================
# 补充说明
# =============================================================================
#
# 1) 为什么「拐过弯的路径」不能作为返回值？
#    dfs 的返回值是要交给父节点继续往上拼的。父节点只通过一条边连到 node，
#    所以站在父节点看，只能「走左边那一支」或「走右边那一支」，不可能同时用上
#    node 的左右两棵子树。因此返回值必须是单侧链；而左右都用的路径只能在 node
#    这里「封顶」，作为答案候选记录下来。
#
# 2) 一个等价的心智模型：把每个节点都想成「某条路径的最高点（拐点）」。
#    那么「以 node 为最高点的最优路径」= max(0, 左子树最佳单侧链) + node.val
#                                             + max(0, 右子树最佳单侧链)，
#    全局答案就是所有节点这个值的最大值。代码里 l_val / r_val 已经自带 max(..., 0)，
#    所以直接相加即可。
#
# 3) 复杂度：每个节点只访问一次，时间 O(n)；额外空间是递归栈，深度为树高 h，
#    最坏情形（一条链）为 O(n)。
#
# 4) 小提示：题目保证树里至少有一个节点。若真传入 root = None，本实现不会更新 ans，
#    最终返回 -inf。
#
# 5) 关于解释器：`TreeNode | None` 这种「类型 | None」的写法需要 Python 3.10 及以上
#    （或用 `from __future__ import annotations`），否则在类定义时就会 TypeError。
#    本仓库根目录带了 .venv（Python 3.11），用它跑即可；若用系统自带的 python3.9 跑，
#    这个文件会在 class Solution 那行直接报错。
#    另外文件顶部的 `from typing import Optional` 其实并未使用（下面的签名写的是
#    `TreeNode | None`），可以删掉。
