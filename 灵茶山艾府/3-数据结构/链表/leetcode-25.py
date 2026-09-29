# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        dummy = ListNode(next=head)
        p0 = dummy

        while n >= k:
            n -= k

            pre = None
            cur = p0.next
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            nxt = p0.next # 第一次循环时， 这个就是1

            p0.next.next = cur
            p0.next = pre

            p0 = nxt  # 第一次循环结束时， 把 p0指向 1，  这样第二次循环时p0 就是 
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    new_head = s.reverseKGroup(head, 2)
    # 输出反转后的链表
    while new_head:
        print(new_head.val, end=" -> ")
        new_head = new_head.next
    print("None")  # 输出 None 表示链表结束