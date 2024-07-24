class Solution:
    def numTrees(self, n: int) -> int:
        numTree = [1] * (n + 1)
        # 0 node = 1 tree
        # 1 node = 1 tree

        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1  # 左子树节点个数
                right = nodes - root  # 右子树节点个数
                total += numTree[left] * numTree[right]
            numTree[nodes] = total  # nodes 个从1到nodes的节点，可以有多少个二叉搜索树
        return numTree[n]


if __name__ == '__main__':
    n = 3
    s = Solution()
    a = s.numTrees(n)
    print(a)
