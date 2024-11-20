# 2516. Take K of Each Character From Left and Right

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count: list[int] = [0, 0, 0]
        for c in s:
            count[ord(c) - ord('a')] += 1

        if min(count) < k:
            return -1

        ans: int = float('inf')
        left = 0
        # Sliding Window [a, a, ... [maxmize the middle of window], ..., b, c]
        for right in range(len(s)):
            count[ord(s[right]) - ord('a')] -= 1

            while min(count) < k:
                count[ord(s[left]) - ord('a')] += 1
                left += 1
            ans = min(ans, len(s) - (right - left + 1))

        return ans


ans = Solution().takeCharacters('aabaaaacaabc', 2)
print(ans)
