# 1208. Get Equal Substrings Within Budget


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans = 0
        start = 0
        cur_cost = 0
        for end in range(len(s)):
            cur_cost += abs(ord(s[end]) - ord(t[end]))
            while cur_cost > maxCost:
                cur_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            ans = max(ans, end - start + 1)

        return ans


ans = Solution().equalSubstring('abcd', 'bcdf', 3)
print(ans)
