# 1963. Minimum Number of Swaps to Make the String Balanced

class Solution:
    def minSwaps(self, s: str) -> int:
        extra_close, max_close = 0, 0
        for c in s:
            if c == "[":
                extra_close -= 1
            else:
                extra_close += 1

            max_close = max(max_close, extra_close)
        return (max_close + 1) // 2


ans = Solution().minSwaps("]]][[[")
print(ans)
