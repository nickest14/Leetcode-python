# 3003. Maximize the Number of Partitions After Operations


from functools import cache


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n: int = len(s)
        masks: list[int] = [1 << (ord(c) - ord("a")) for c in s]

        @cache
        def dp(i: int, can_change: bool, mask: int) -> int:
            if i == n:
                return 0
            new_mask: int = mask | masks[i]
            ans: int = 0

            if new_mask.bit_count() > k:
                ans = 1 + dp(i + 1, can_change, masks[i])
            else:
                ans = dp(i + 1, can_change, new_mask)

            if can_change:
                for j in range(26):
                    changed_mask: int = mask | (1 << j)
                    if changed_mask.bit_count() > k:
                        ans = max(ans, 1 + dp(i + 1, False, 1 << j))
                    else:
                        ans = max(ans, dp(i + 1, False, changed_mask))
            return ans

        return dp(0, True, 0) + 1


ans = Solution().maxPartitionsAfterOperations("accca", 2)
print(ans)
