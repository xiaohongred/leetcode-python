from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    LeetCode 968. 监控二叉树

    在二叉树的节点上安装摄像头，每个摄像头能覆盖【自己、父节点、直接子节点】三类节点。
    求覆盖所有节点所需的最少摄像头数量。

    这是树形 DP，可以看成 337 题（打家劫舍 III）的加强版：
        * 337 题：约束是「父子不能同时选」，是单向的，一个 bit（选 / 不选）就够；
        * 本题  ：约束是「每个节点都必须被覆盖」，而覆盖关系是**双向**的
                  —— 父节点可以覆盖子节点，子节点也可以覆盖父节点，
                  所以必须多一个维度，记录「这个节点究竟是被谁覆盖的」。

    ── dfs(node) 返回三个数 ────────────────────────────────────────────
        chose       ：node【自己装了摄像头】时，以 node 为根的子树所需的最少摄像头数
        by_fa      ：node 不装，且它【由父节点覆盖】时，子树所需的最少摄像头数
        by_children：node 不装，且它【由某个孩子覆盖】时，子树所需的最少摄像头数

    「谁负责覆盖 node」只有自己、父亲、孩子这三种，互斥且穷尽，所以三个状态够用。

    ── 转移的关键规则 ──────────────────────────────────────────────────
    先记住一句话：**只要 node 没装摄像头，它的孩子就不可能是 by_fa 状态**
    （孩子的 by_fa 意为「被自己的父亲覆盖」，而它的父亲正是不装摄像头的 node）。

    于是三个转移可以列成一张表：
        node 的状态    有没有摄像头    孩子允许的状态                对孩子的要求
        chose          有             chose / by_fa / by_children  无（node 会覆盖孩子）
        by_fa          无             chose / by_children          孩子各自照顾好自己
        by_children    无             chose / by_children          至少一个孩子装摄像头
    """

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            """
            返回三维组 (chose, by_fa, by_children)，含义见类注释。
            三个值都只统计【以 node 为根的子树内部】的摄像头数量。
            """
            if node is None:
                # 空节点的边界值：
                #   chose       = inf：空节点不可能装摄像头，这个状态不存在；
                #   by_fa       = 0  ：空节点「由父节点覆盖」，它这棵（空）子树自然 0 个摄像头；
                #   by_children = 0  ：只是表示「这一侧无须操心」，细节见末尾说明。
                return float('inf'), 0, 0

            l_choose, l_by_fa, l_by_children = dfs(node.left)
            r_choose, r_by_fa, r_by_children = dfs(node.right)

            # ① node 自己装摄像头：node 自己就被覆盖了，还会顺带覆盖两个孩子，
            #    所以孩子完全自由 —— 三种状态任选，各自取 min。
            #    最后的 +1 就是 node 这台摄像头。
            chose = min(l_choose, l_by_fa, l_by_children) + min(r_choose, r_by_fa, r_by_children) + 1

            # ② node 不装、由父节点覆盖：node 自己不用孩子操心，
            #    但孩子也不能指望 node（node 没摄像头），所以孩子只能在
            #    「自己装」或「靠自己的孩子」里选 —— 不允许 by_fa。
            by_fa = min(l_choose, l_by_children) + min(r_choose, r_by_children)

            # ③ node 不装、又没有父节点帮忙，那 node 必须被某个孩子覆盖，
            #    也就是左右孩子里【至少一个装摄像头】。只有三种搭配：
            #       左装 + 右靠它的孩子 / 左靠它的孩子 + 右装 / 左右都装
            #    注意「左靠孩子 + 右靠孩子」不合法 —— 那样没人覆盖 node 自己。
            by_children = min(l_choose + r_by_children, l_by_children + r_choose, l_choose + r_choose)

            return chose, by_fa, by_children

        chose, _, by_children = dfs(root)
        # 根节点没有父节点，所以 by_fa 这个状态对根不存在，只需在另外两个里取 min。
        return min(chose, by_children)


if __name__ == "__main__":
    s = Solution()
    # 结构是 路径 B - A - 根 - C（值都是 0，无关紧要）：
    # 在 A 和 C 上各装一台即可全覆盖，所以答案是 2
    print(s.minCameraCover(TreeNode(0, TreeNode(0, None, TreeNode(0)), TreeNode(0))))


# =============================================================================
# 补充说明
# =============================================================================
#
# 1) 空节点的边界值 (inf, 0, 0) 为什么是对的？拿一个叶子验算就清楚了。
#    叶子的左右孩子都是 None，即 l = r = (inf, 0, 0)，于是：
#        chose       = min(inf,0,0) + min(inf,0,0) + 1 = 1     装 1 台，正确
#        by_fa       = min(inf,0)   + min(inf,0)         = 0   靠父节点罩，自己不用装
#        by_children = min(inf+0, 0+inf, inf+inf)        = inf  叶子没有孩子，不可能靠孩子覆盖
#    三个值都符合直觉，其中 by_children = inf 正是「不可能」的体现。
#
# 2) 那空节点的 by_children 为什么写 0 而不是 inf？
#    它并不表示「空节点被子节点覆盖」，只是表示「这一侧无须操心」。
#    它只会出现在 `l_by_children + r_choose` 这类项里，而那一项能成立的前提
#    恰恰是另一侧真的装了摄像头（比如左孩子为空、右孩子装摄像头覆盖 node），
#    所以 node 一定被覆盖，不会算出偏小的结果。
#
# 3) 为什么「只要 node 没装摄像头，孩子就不能是 by_fa」？
#    孩子的 by_fa 表示「它由自己的父亲覆盖」，而它的父亲就是 node；
#    node 既然没装摄像头，这个覆盖关系根本不存在。
#    这也解释了为什么 by_fa 只出现在第 ① 条（node 自己装）里。
#
# 4) 为什么 by_children 里没有 `l_by_children + r_by_children` 这一项？
#    那两个孩子都在指望自己的孩子，谁也没装摄像头，于是 node 无人覆盖 —— 非法。
#
# 5) 复杂度：每个节点只访问一次，时间 O(n)；额外空间是递归栈，深度为树高 h，
#    最坏（链状树）O(n)。
#
# 6) 与 337 题对照：337 题只需要「选 / 不选」两个状态，因为约束是单向的
#    （选了父节点就禁止选孩子）；本题的覆盖是双向的，必须额外记录
#    「谁覆盖了我」，这就是状态从两个涨到三个的原因。
