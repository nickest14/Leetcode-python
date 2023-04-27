# 572. Subtree of Another Tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_equal(node1: TreeNode, node2: TreeNode):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and is_equal(node1.left, node2.left) \
                and is_equal(node1.right, node2.right)

        if not root:
            return False
        return is_equal(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

sub_root = TreeNode(4)
sub_root.left = TreeNode(1)
sub_root.right = TreeNode(2)

ans = Solution().isSubtree(root, sub_root)
print(ans)
