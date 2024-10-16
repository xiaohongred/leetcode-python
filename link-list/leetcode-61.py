# Definition for singly-linked list.
from typing import Optional
import tools


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        # get length
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length

        if k == 0:
            return head

        # move to the pivot and rotate
        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        newHead = cur.next
        cur.next = None
        tail.next = head  # 原始数组的末尾指向原始数组的头部
        return newHead


if __name__ == '__main__':
    s = Solution()
    head = [1, 2, 3, 4, 5]
    k = 2
    head = tools.buildList(head)
    a = s.rotateRight(head, k)
    tools.printList(a)

    head = [0, 1, 2]
    k = 4
    head = tools.buildList(head)
    a = s.rotateRight(head, k)
    tools.printList(a)
