# 1367. Linked List in Binary Tree

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def check_path(head, root):
            if not head:
                return True
            if not root or head.val != root.val:
                return False
            return check_path(head.next, root.left) or check_path(head.next, root.right)

        if not root:
            return False
        if check_path(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(8)

root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(8)
root.right.left.right.left = TreeNode(1)
root.right.left.right.right = TreeNode(3)
ans = Solution().isSubPath(head, root)
print(ans)
