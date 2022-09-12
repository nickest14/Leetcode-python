# 234. Palindrome Linked List

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head.next:
            return True
        walker = runner = head
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
        if runner:
            walker = walker.next
        reverse = walker
        while walker.next:
            node = walker.next
            walker.next = node.next
            node.next = reverse
            reverse = node
        while head and reverse and head.val == reverse.val:
            head = head.next
            reverse = reverse.next
        return not reverse

# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         val = []
#         while head:
#             val.append(head.val)
#             head = head.next
#         return val == val[::-1]


# l6 = ListNode(val=6)
# l5 = ListNode(val=5, next=l6)
# l4 = ListNode(val=4, next=l5)
# l3 = ListNode(val=3, next=l4)
# l2 = ListNode(val=2, next=l3)
# l1 = ListNode(val=1, next=l2)

l9 = ListNode(val=1)
l8 = ListNode(val=2, next=l9)
l7 = ListNode(val=3, next=l8)
l6 = ListNode(val=4, next=l7)
l5 = ListNode(val=5, next=l6)
l4 = ListNode(val=4, next=l5)
l3 = ListNode(val=3, next=l4)
l2 = ListNode(val=2, next=l3)
l1 = ListNode(val=1, next=l2)
ans = Solution().isPalindrome(l1)
print(ans)
