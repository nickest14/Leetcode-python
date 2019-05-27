# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if root:
            ans = []
            nodes = []
            nodes.append(root)
            while nodes:
                level_li = []
                temp_nodes = []
                for i in nodes:
                    level_li.append(i.val)
                    if i.left:
                        temp_nodes.append(i.left)
                    if i.right:
                        temp_nodes.append(i.right)
                ans.append(level_li)
                nodes = temp_nodes
            return ans
        return []


root = TreeNode(3)
root1 = TreeNode(9)
root2 = TreeNode(20)
root3 = TreeNode(15)
root4 = TreeNode(7)
root.left = root1
root.right = root2
root.right.left = root3
root.right.right = root4

ans = Solution().levelOrder(root)
print(ans)
