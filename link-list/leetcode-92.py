# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional
import tools


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # find left
        prev, cur = dummy, head
        for i in range(left - 1):
            prev = cur
            cur = cur.next
        # now cur = "left", LP="node before left"
        
        LP = prev

        p = None
        # reverse from left to right
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = p
            p = cur
            cur = tmpNext

        # 把反转之后的链表加在整体链表中去
        LP.next.next = cur
        LP.next = p
        return dummy.next


if __name__ == '__main__':
    s = Solution()

    head = [1, 2, 3, 4, 5]
    left = 2
    right = 4
    head = tools.buildList(head)
    a = s.reverseBetween(head, left, right)
    tools.printList(a)

    head = [5]
    left = 1
    right = 1
    head = tools.buildList(head)
    a = s.reverseBetween(head, left, right)
    tools.printList(a)
