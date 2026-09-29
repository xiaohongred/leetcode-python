# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 快慢指针（Floyd 判圈算法），分两个阶段

        # ---------- 阶段一：判断是否有环，并找到相遇点 ----------
        slow = head  # 慢指针，每次走 1 步
        fast = head  # 快指针，每次走 2 步

        # fast 每次跳两步，所以必须保证 fast 和 fast.next 都非空，
        # 否则 fast.next.next 会报错（走到链表尾部说明无环）
        while fast and fast.next:
            slow = slow.next          # 慢指针走 1 步
            fast = fast.next.next     # 快指针走 2 步

            # 两指针相遇，说明存在环
            if fast is slow:
                # ---------- 阶段二：找环的入口节点 ----------
                # 数学结论：
                #   设 头到环入口距离为 a，环入口到相遇点距离为 b，
                #   相遇点再走回环入口距离为 c（环长 = b + c）。
                #
                #   图示：
                #     head ──a──> 环入口 ──b──> 相遇点
                #                   ↑              │
                #                   └──── c ───────┘
                #
                #   相遇时两指针各走了多远：
                #     慢指针（每次 1 步）：走了 a + b
                #     快指针（每次 2 步）：走了 a + b + n*(b + c)
                #       （n 为快指针在环里多转的整圈数）
                #
                #   因为快指针路程是慢指针的 2 倍：
                #       2(a + b) = a + b + n*(b + c)
                #
                #   化简（两边同减 a + b）：
                #       a + b = n*(b + c)
                #
                #   移项并拆分 n*(b + c)：
                #       a = n*(b + c) - b
                #         = (n - 1)*(b + c) + (b + c) - b
                #         = (n - 1)*(b + c) + c
                #
                #   即：a = c + (n - 1)*(b + c)
                #
                #   这个式子在说什么：
                #     - 右边 c + (n-1)*(b+c)：从「相遇点」出发，先走 c 步
                #       到达环入口，再多绕 (n-1) 整圈，仍然回到环入口。
                #       也就是：从相遇点走 a 步一定能到环入口。
                #       （注意：其实从相遇点走 c 步也能到入口，因为 a 比 c
                #         多了 (n-1) 整圈，而环上多绕整圈不改变落点。
                #         这里用 a 是因为 head 到入口正好是 a 步，
                #         两指针同速走 a 步后才会在入口「同时」相遇。）
                #     - 左边 a：恰好是「从头出发走到环入口」的距离。
                #
                #   结论：
                #     一个指针从 head 出发，另一个指针从「相遇点」继续走，
                #     两者速度相同（每次 1 步），走 a 步后都会同时到达环入口，
                #     因此它们第一次相遇的位置就是环的入口节点。
                #
                #   为什么一定是「第一次」到达环入口就相遇？两个理由：
                #     ① 步数相同、速度相同 → 同时到达
                #        - head 指针从头出发，到环入口正好要走 a 步；
                #        - 相遇点指针由上面的公式 a = c + (n-1)*(b+c) 可知，
                #          也正好要走 a 步。
                #        - 两者每步都走 1 格，所以第 a 步时会「同时」落在环入口。
                #
                #     ② 在 head 到达入口之前，两者不可能相遇
                #        - head 到达入口前一直走在「环外的尾巴」上；
                #        - 相遇点指针一开始就在「环内」走；
                #        - 尾巴和环唯一的重合点就是「环入口」，
                #          所以入口之前两者所在节点没有交集，不可能提前相遇。
                #
                #   一个小细节：
                #     相遇点指针往前走时，可能中途已经路过环入口好几次
                #     （当 a 很大时，它会先绕几圈）。但这没关系——它路过时
                #     head 还没到，两指针不相等，循环不会停；只有 head 第一次
                #     走到入口时，两者才真正相等、循环退出。
                while slow is not head:
                    slow = slow.next   # 相遇点指针每次走 1 步
                    head = head.next   # 头指针每次走 1 步

                return slow            # 相遇处即为环的入口节点

        # 循环正常结束（fast 走到 None），说明链表无环
        return None


if __name__ == "__main__":
    s = Solution()
    # 创建一个有环链表: 1 -> 2 -> 3 -> 4 -> 5 -> 2 (环)
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2  # 创建环（环入口是 node2）

    cycle_node = s.detectCycle(head)
    if cycle_node:
        print(cycle_node.val)  # 输出环的起点节点的值，应为 2
    else:
        print("No cycle detected")