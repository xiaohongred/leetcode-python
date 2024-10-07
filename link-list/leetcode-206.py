# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional
import tools


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def reverseListV2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseListV2(head.next)  # 反转剩下的元素
            head.next.next = head  # 反转当前的元素
        head.next = None
        return newHead


if __name__ == '__main__':
    s = Solution()

    l = [1, 2, 3, 4, 50]
    head = tools.buildList(l)
    tools.printList(head)
    newHead = s.reverseList(head)
    tools.printList(newHead)

    l = [1, 2]
    head = tools.buildList(l)
    tools.printList(head)
    newHead = s.reverseList(head)
    tools.printList(newHead)

    l = []
    head = tools.buildList(l)
    tools.printList(head)
    newHead = s.reverseList(head)
    tools.printList(newHead)
