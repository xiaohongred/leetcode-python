# Definition for singly-linked list.
from typing import Optional
import tools


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr and curr.next:
            # save ptrs
            nxtPair = curr.next.next

            second = curr.next

            # reverse this pair
            second.next = curr
            curr.next = nxtPair
            prev.next = second

            # update ptrs
            prev = curr
            curr = nxtPair
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    head = [1, 2, 3, 4]
    head = tools.buildList(head)
    a = s.swapPairs(head)
    tools.printList(a)

    head = []
    head = tools.buildList(head)
    a = s.swapPairs(head)
    tools.printList(a)

    head = [1]
    head = tools.buildList(head)
    a = s.swapPairs(head)
    tools.printList(a)
