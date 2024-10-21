# Definition for singly-linked list.
from typing import Optional
import tools


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = head

        cur = head.next  # 从第二元素开始
        prev = head

        while cur:
            if cur.val >= prev.val:
                prev, cur = cur, cur.next
                continue
            tmp = dummyHead
            while cur.val > tmp.next.val:
                tmp = tmp.next
            prev.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = prev.next
        return dummyHead.next


if __name__ == '__main__':
    s = Solution()
    head = [4, 2, 1, 3]
    head = tools.buildList(head)
    a = s.insertionSortList(head)
    tools.printList(a)

    head = [-1, 5, 3, 4, 0]
    head = tools.buildList(head)
    a = s.insertionSortList(head)
    tools.printList(a)
