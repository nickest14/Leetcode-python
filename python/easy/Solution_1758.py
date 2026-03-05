# 1758. Minimum Changes To Make Alternating Binary String


class Solution:
    def minOperations(self, s: str) -> int:
        def count_changes_if_start_with(first_char: str) -> int:
            changes: int = 0
            for i in range(len(s)):
                if i % 2 == 0 and s[i] != first_char:
                    changes += 1
                elif i % 2 == 1 and s[i] == first_char:
                    changes += 1
            return changes

        changes_0: int = count_changes_if_start_with("0")
        changes_1: int = count_changes_if_start_with("1")
        return min(changes_0, changes_1)


ans = Solution().minOperations("0100")
print(ans)
