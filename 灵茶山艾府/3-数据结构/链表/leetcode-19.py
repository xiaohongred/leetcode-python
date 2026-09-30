# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(next=head)
        right = dummy
        for _ in range(n):
            right = right.next
        
        left = dummy
        while right.next:
            right = right.next
            left = left.next
        
        left.next = left.next.next
        return dummy.next


if __name__ == "__main__":
    pass