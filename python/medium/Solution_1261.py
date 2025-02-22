# 1261. Find Elements in a Contaminated Binary Tree

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.nodes = set()
        root.val = 0
        self._recover(root)

    def _recover(self, root: TreeNode = None):
        if not root:
            return

        self.nodes.add(root.val)

        if root.left:
            root.left.val = root.val * 2 + 1
            self._recover(root.left)
        if root.right:
            root.right.val = root.val * 2 + 2
            self._recover(root.right)

    def find(self, target: int) -> bool:
        return target in self.nodes


root = TreeNode(-1)
root.right = TreeNode(-1)
root.right.left = TreeNode(-1)
root.right.left = TreeNode(-1)
root.right.left.left = TreeNode(-1)

obj = FindElements(root)
print(obj.find(2))
print(obj.find(3))
print(obj.find(4))
print(obj.find(5))
