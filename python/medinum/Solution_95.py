# 95. Unique Binary Search Trees II


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTreesDFS(self, left, right):
        if left > right:
            return [None]
        ans = []
        for i in range(left, right + 1):
            left_nodes = self.generateTreesDFS(left, i - 1)
            right_nodes = self.generateTreesDFS(i + 1, right)
            for left_node in left_nodes:
                for right_node in right_nodes:
                    root = TreeNode(i)
                    root.left = left_node
                    root.right = right_node
                    ans.append(root)
        return ans

    def generateTrees(self, n: int):
        if n == 0:
            return []
        return self.generateTreesDFS(1, n)


ans = Solution().generateTrees(3)
print(ans)
