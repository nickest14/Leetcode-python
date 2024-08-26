# 145. Binary Tree Postorder Traversal

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        ans: list[int] = []

        bag: list[TreeNode] = [root]
        while bag:
            node = bag.pop()
            ans.append(node.val)
            if node.left:
                bag.append(node.left)
            if node.right:
                bag.append(node.right)

        return ans[::-1]

    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        stack, result = [], []
        while stack or root:
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left
            node = stack.pop()
            if stack and stack[-1] is node.right:
                root = stack.pop()
                stack.append(node)
            else:
                result.append(node.val)
        return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)

ans = Solution().postorderTraversal(root)
print(ans)
