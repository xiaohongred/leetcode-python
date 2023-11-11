from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev

    def reverseListNest(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseListNest(head.next)
            head.next.next = head
        head.next = None

        return newHead


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    head = ListNode(-1, None)
    cur = head
    for item in nums:
        cur.next = ListNode(item, None)
        cur = cur.next
    print(head)
    head = head.next
    s = Solution()
    newHead = s.reverseListNest(head)
    print(newHead.val)
