# 133. Clone Graph
import collections

# Definition for a Node.


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    # BFS version
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        queue = collections.deque()
        hash_dict = dict()
        node_copy = Node(node.val, [])
        hash_dict[node] = node_copy
        queue.append(node)
        while queue:
            current_node = queue.popleft()
            if current_node is None:
                break
            for i in current_node.neighbors:
                if i not in hash_dict:
                    hash_dict[i] = Node(i.val, [])
                    queue.append(i)
                hash_dict[current_node].neighbors.append(hash_dict[i])
        return node_copy

    # DFS version
    def cloneGraph_2(self, node: 'Node') -> 'Node':
        hash_dict = dict()
        node_copy = self.dfs(node, hash_dict)
        return node_copy

    def dfs(self, node, hash_dict):
        if not node:
            return None
        if node in hash_dict.keys():
            return hash_dict[node]
        node_copy = Node(node.val, [])
        hash_dict[node] = node_copy
        for n in node.neighbors:
            n_copy = self.dfs(n, hash_dict)
            if n_copy:
                node_copy.neighbors.append(n_copy)
        return node_copy


node1 = Node(1, [])
node2 = Node(2, [])
node3 = Node(3, [])
node4 = Node(4, [])
node1.neighbors = [node2, node3]
node2.neighbors = [node1, node4]
node3.neighbors = [node1, node4]
node4.neighbors = [node2, node3]
ans = Solution().cloneGraph(node1)
print(ans)
