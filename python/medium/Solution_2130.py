# 2130. Maximum Twin Sum of a Linked List

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Original
        # 6 -> 5 -> 4 -> 3-> 2 -> 1

        # After adjust become
        # 6 <- 5 <- 4 | 3 -> 2 -> 1
        # the pair becomes (4, 3), (5, 2), (6, 1)
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        ans = 0
        while slow:
            ans = max(ans, slow.val + prev.val)
            slow = slow.next
            prev = prev.next
        return ans


head = ListNode(5)
head.next = ListNode(4)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
ans = Solution().pairSum(head)
print(ans)