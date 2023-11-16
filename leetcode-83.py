from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = head
        if head is None:
            return head
        if head.next is None:
            return head

        cur = head.next
        while cur:
            if cur.val == pre.val:
                pre.next = cur.next
                cur = cur.next
            else:
                pre = cur
                cur = cur.next

        return head


if __name__ == '__main__':
    pass
