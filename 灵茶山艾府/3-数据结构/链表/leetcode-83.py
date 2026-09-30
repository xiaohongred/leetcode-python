# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return head
        
        cur = head
        while cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    new_head = s.deleteDuplicates(head)
    # 输出去重后的链表
    while new_head:
        print(new_head.val, end=" -> ")
        new_head = new_head.next
    print("None")  # 输出 None 表示链表结束