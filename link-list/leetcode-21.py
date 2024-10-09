# Definition for singly-linked list.
from typing import Optional
import tools


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        tail = dummyHead

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummyHead.next


if __name__ == '__main__':
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]

    head1 = tools.buildList(l1)
    head2 = tools.buildList(l2)
    s = Solution()

    a = s.mergeTwoLists(head1, head2)
    tools.printList(a)

    l1 = []
    l2 = []
    head1 = tools.buildList(l1)
    head2 = tools.buildList(l2)
    a = s.mergeTwoLists(head1, head2)
    tools.printList(a)

    l1 = []
    l2 = [0]
    head1 = tools.buildList(l1)
    head2 = tools.buildList(l2)
    a = s.mergeTwoLists(head1, head2)
    tools.printList(a)
