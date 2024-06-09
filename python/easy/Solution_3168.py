# 3168. Minimum Number of Chairs in a Waiting Room


class Solution:
    def minimumChairs(self, s: str) -> int:
        ans, remain = 0, 0
        for c in s:
            if c == 'E':
                if remain:
                    remain -= 1
                else:
                    ans += 1
            else:
                remain += 1

        return ans



ans = Solution().minimumChairs('ELELEEL')
print(ans)
