# 3085. Minimum Deletions to Make String K-Special

from collections import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq: dict[str, int] = Counter(word)
        ans: int = len(word)
        for ref_count in freq.values():
            changed: int = 0
            for count in freq.values():
                if count < ref_count:
                    changed += count
                elif count - ref_count > k:
                    changed += count - ref_count - k
            ans = min(ans, changed)
        return ans


ans = Solution().minimumDeletions("aabcaba", 0)
# ans = Solution().minimumDeletions("dabdcbdcdcd", 2)
print(ans)
