# 92. Reverse Linked List II

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None or m >= n:
            return head
        root = ListNode(0)
        root.next = head
        previous = root
        count = 1

        while previous.next and count < m:
            count += 1
            previous = previous.next
        m_node = previous.next
        current = m_node.next
        while current and count < n:
            next = current.next
            current.next = previous.next
            previous.next = current
            m_node.next = next
            current = next
            count += 1
        return root.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

ans = Solution().reverseBetween(node1, 3, 5)
while ans:
    print(ans.val)
    if ans.next:
        ans = ans.next
    else:
        ans = None
# print(ans)
