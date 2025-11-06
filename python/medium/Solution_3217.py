# 3217. Delete Nodes From Linked List Present in Array

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        num_set = set(nums)
        dummy: ListNode = ListNode()
        current = dummy

        while head:
            if head.val not in num_set:
                current.next = head
                current = current.next
            head = head.next

        current.next = None
        return dummy.next


node: ListNode = ListNode(1)
node2 = node.next = ListNode(2)
node3 = node2.next = ListNode(3)
node4 = node3.next = ListNode(4)
ans = Solution().modifiedList(nums=[1, 2, 3], head=node)
print(ans)
