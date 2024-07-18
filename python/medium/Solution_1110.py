# 1110. Delete Nodes And Return Forest

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(node: TreeNode, is_root):
            if not node:
                return None

            deleted: bool = node.val in delete_set
            if is_root and not deleted:
                remain_nodes.append(node)

            node.left = dfs(node.left, deleted)
            node.right = dfs(node.right, deleted)

            return None if deleted else node

        delete_set: set = set(to_delete)
        remain_nodes: list[TreeNode] = []
        dfs(root, True)

        return remain_nodes


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
ans = Solution().delNodes(root, [3, 5])
print(ans)
