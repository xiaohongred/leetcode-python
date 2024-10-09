from typing import Optional
import tools


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] != nums[right]:
                return False
            left += 1
            right -= 1
        return True

    def isPalindromeV2(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half list
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


if __name__ == '__main__':
    s = Solution()
    l = [1, 2, 2, 1]
    head = tools.buildList(l)
    a = s.isPalindrome(head)
    print(a)

    l = [1, 2]
    head = tools.buildList(l)
    a = s.isPalindrome(head)
    print(a)

    l = [1, 2, 2, 1]
    head = tools.buildList(l)
    a = s.isPalindromeV2(head)
    print(a)

    l = [1, 2]
    head = tools.buildList(l)
    a = s.isPalindromeV2(head)
    print(a)
