# Definition for singly-linked list.
from typing import Optional
import tools


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next

            fast = fast.next
            fast = fast.next
            if slow == fast:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    head = [3, 2, 0, -4]
    pos = 1
    head = tools.buildCircleList(head, pos)
    a = s.hasCycle(head)
    print(a)

    head = [1, 2]
    pos = 0
    head = tools.buildCircleList(head, pos)
    a = s.hasCycle(head)
    print(a)

    head = [1]
    pos = -1
    head = tools.buildCircleList(head, pos)
    a = s.hasCycle(head)
    print(a)
