# 1653. Minimum Deletions to Make String Balanced


class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack_b: int = 0
        deletions: int = 0
        for c in s:
            if stack_b and c == "a":
                stack_b -= 1
                deletions += 1
            elif c == "b":
                stack_b += 1
        return deletions


ans = Solution().minimumDeletions("aababbab")
ans = Solution().minimumDeletions("aabbbbbaaab")
print(ans)
