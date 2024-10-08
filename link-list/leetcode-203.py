from typing import Optional
import tools


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = head

        prev, curr = dummyHead, dummyHead.next
        while curr:
            if curr.val == val:
                curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return dummyHead.next


if __name__ == '__main__':
    s = Solution()
    l = [1, 2, 6, 3, 4, 5, 6]
    val = 6
    head = tools.buildList(l)
    a = s.removeElements(head, val)
    tools.printList(a)

    l = []
    val = 1
    head = tools.buildList(l)
    a = s.removeElements(head, val)
    tools.printList(a)

    l = [7, 7, 7, 7]
    val = 7
    head = tools.buildList(l)
    a = s.removeElements(head, val)
    tools.printList(a)
