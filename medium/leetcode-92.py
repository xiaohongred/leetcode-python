# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # 1) reach node at position "left"
        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next

        # cur = "left", leftPrev="node before left"
        # 2) reverse from left to right
        prev = None
        for i in range(right - left + 1):  # 需要调转三个箭头
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp

        # 3) update pointers
        leftPrev.next.next = cur
        leftPrev.next = prev

        return dummy.next


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    left = 2
    right = 4
