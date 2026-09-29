# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast is slow:
                return True
            
        return False


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
    node5.next = node2  # 创建环

    print(s.hasCycle(head))  # 输出 True