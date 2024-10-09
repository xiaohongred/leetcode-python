import tools


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            mod = (c + l1.val + l2.val) % 10
            c = (c + l1.val + l2.val) // 10
            tail.next = ListNode(mod, None)
            tail = tail.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            mod = (c + l1.val) % 10
            c = (c + l1.val) // 10
            tail.next = ListNode(mod, None)
            tail = tail.next
            l1 = l1.next
        while l2:
            mod = (c + l2.val) % 10
            c = (c + l2.val) // 10
            tail.next = ListNode(mod, None)
            tail = tail.next
            l2 = l2.next
        if c:
            tail.next = ListNode(c, None)
            
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]

    head1 = tools.buildList(l1)
    head2 = tools.buildList(l2)

    a = s.addTwoNumbers(head1, head2)
    tools.printList(a)

    l1 = [0]
    l2 = [0]
    head1 = tools.buildList(l1)
    head2 = tools.buildList(l2)
    a = s.addTwoNumbers(head1, head2)
    tools.printList(a)

    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    head1 = tools.buildList(l1)
    head2 = tools.buildList(l2)
    a = s.addTwoNumbers(head1, head2)
    tools.printList(a)
