# Definition for singly-linked list.
from typing import Optional
import tools


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None  # 最后一个元素指向null
        prev = None
        while second:  # reverse last half list  反转链表的后半部分
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

        #  1 -> 2 -> 3 -> 4

        # first          second
        #  1 -> 2 ->  3 <- 4

        #     tmp1, tmp2 = first.next, second.next
        #  1 -> 2 ->  3 <- 4

        #  1->4          first.next = second
        #  4->2           second.next = tmp1
        #           first = tmp1
        #                second = tmp2
        #  1 -> 4 -> 2 -> 3


if __name__ == '__main__':
    l = [1, 2, 3, 4]
    head = tools.buildList(l)
    s = Solution()
    tools.printList(head)
    s.reorderList(head)
    tools.printList(head)

    l = [1, 2, 3, 4, 5]
    head = tools.buildList(l)
    tools.printList(head)
    s.reorderList(head)
    tools.printList(head)
