# 2181. Merge Nodes in Between Zeros

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = cur_node = ListNode(val=-1)
        curr = head.next
        val = 0
        while curr:
            if curr.val == 0:
                node = ListNode(val=val)
                cur_node.next = node
                cur_node = node
                val = 0
            else:
                val += curr.val

            curr = curr.next

        return ans.next


curr = head = ListNode(val=0)
for val in [3, 1, 0, 4, 5, 2, 0]:
    curr.next = ListNode(val=val)
    curr = curr.next

ans = Solution().mergeNodes(head)
print(ans)
