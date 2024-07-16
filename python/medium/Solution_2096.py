# 2096. Step-By-Step Directions From a Binary Tree Node to Another

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        nodes_parents: dict[int, TreeNode] = {}
        q: list[TreeNode] = [root]
        while q:
            cur_node = q.pop()
            if cur_node.val == startValue:
                start_node = cur_node
            if cur_node.left:
                nodes_parents[cur_node.left.val] = cur_node
                q.append(cur_node.left)
            if cur_node.right:
                nodes_parents[cur_node.right.val] = cur_node
                q.append(cur_node.right)

        visited = set()
        q = [start_node]
        tracked_path: dict[TreeNode, tuple(TreeNode, str)] = {}
        while q:
            cur_node = q.pop()
            visited.add(cur_node)

            if cur_node.val == destValue:
                destination_node = cur_node
                break

            if cur_node.val in nodes_parents and nodes_parents[cur_node.val] not in visited:
                parent = nodes_parents[cur_node.val]
                q.append(parent)
                tracked_path[parent] = (cur_node, 'U')
            if cur_node.left and cur_node.left not in visited:
                q.append(cur_node.left)
                tracked_path[cur_node.left] = (cur_node, 'L')
            if cur_node.right and cur_node.right not in visited:
                q.append(cur_node.right)
                tracked_path[cur_node.right] = (cur_node, 'R')

        result_path: list[str] = []
        cur_node = destination_node
        while cur_node != start_node:
            source_node, direction = tracked_path[cur_node]
            result_path.append(direction)
            cur_node = source_node
        result_path.reverse()
        return ''.join(result_path)


root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(4)
ans = Solution().getDirections(root, 3, 6)
# ans = Solution().getDirections(root, 1, 3)
# ans = Solution().getDirections(root, 5, 4)
print(ans)
