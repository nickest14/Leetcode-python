# 1290. Convert Binary Number in a Linked List to Integer

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        s: str = ""
        while head:
            s += str(head.val)
            head = head.next
        return int(s, 2)


node = ListNode(1)
node.next = ListNode(0)
node.next.next = ListNode(1)

ans = Solution().getDecimalValue(node)
print(ans)
