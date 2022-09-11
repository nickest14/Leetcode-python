# 206. Reverse Linked List

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        while head:
            node = head.next
            head.next = new_head
            new_head = head
            head = node
        return new_head

l6 = ListNode(val=6)
l5 = ListNode(val=5, next=l6)
l4 = ListNode(val=4, next=l5)
l3 = ListNode(val=3, next=l4)
l2 = ListNode(val=2, next=l3)
l1 = ListNode(val=1, next=l2)

ans = Solution().reverseList(l1)
while ans:
    print(ans.val)
    ans = ans.next
