# 86. Partition List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left_head = ListNode(0)
        left_begin = left_head
        right_head = ListNode(0)
        right_begin = right_head
        while head:
            if head.val < x:
                left_head.next = ListNode(head.val)
                left_head = left_head.next
            else:
                right_head.next = ListNode(head.val)
                right_head = right_head.next
            head = head.next
        left_head.next = right_begin.next
        return left_begin.next


node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(5)
node6 = ListNode(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

ans = Solution().partition(node1, 3)
while ans:
    print(ans.val)
    if ans.next:
        ans = ans.next
    else:
        ans = None
# print(ans)
