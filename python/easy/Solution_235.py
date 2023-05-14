# 235. Lowest Common Ancestor of a Binary Search Tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        while root:
            if root.val < p.val:
                root = root.right
            elif root.val > q.val:
                root = root.left
            else:
                break
        return root


root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = p = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = q = TreeNode(5)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)


ans = Solution().lowestCommonAncestor(root, p, q)
print(ans)
