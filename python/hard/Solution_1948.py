# 1948. Delete Duplicate Folders in System

from typing import List
from collections import defaultdict


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        tree: dict[str, dict] = {}
        for path in paths:
            node: dict[str, dict] = tree
            for folder in path:
                node = node.setdefault(folder, {})

        duplicates: defaultdict[str, list[dict[str, dict]]] = defaultdict(list)

        def serialize(node: dict[str, dict]) -> str:
            if not node:
                return "()"

            children_serialization: str = "".join(
                child + serialize(child_node)
                for child, child_node in sorted(node.items())
            )
            
            serial: str = "(" + children_serialization + ")"
            duplicates[serial].append(node)
            return serial

        serialize(tree)
        for nodes in duplicates.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.clear()  # Remove all subfolders.
                    node["#"] = True  # Mark the node as deleted.

        ans: list[list[str]] = []

        def collect_paths(node: dict[str, dict], path: list[str]):
            for child_name, child_node in node.items():
                if "#" in child_node:
                    continue
                new_path = path + [child_name]
                ans.append(new_path)
                collect_paths(child_node, new_path)

        collect_paths(tree, [])
        return ans


ans = Solution().deleteDuplicateFolder(
    [["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]
)
print(ans)
