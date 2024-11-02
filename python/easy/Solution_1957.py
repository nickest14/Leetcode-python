# 1957. Delete Characters to Make Fancy String


class Solution:
    def makeFancyString(self, s: str) -> str:
        ans: str = s[:2]
        for c in s[2:]:
            if not (ans[-1] == ans[-2] == c):
                ans += c

        return ans


# ans = Solution().makeFancyString('se')
ans = Solution().makeFancyString('leeetcode')
print(ans)
