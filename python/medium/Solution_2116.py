# 2116. Check if a Parentheses String Can Be Valid


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n: int = len(s)
        if n % 2 == 1:
            return False

        open_count: int = 0
        for i in range(n):
            if s[i] == "(" or locked[i] == "0":
                open_count += 1
            else:
                open_count -= 1

            if open_count < 0:
                return False

        close_count: int = 0
        for i in range(n - 1, -1, -1):
            if s[i] == ")" or locked[i] == "0":
                close_count += 1
            else:
                close_count -= 1

            if close_count < 0:
                return False

        return True


ans = Solution().canBeValid("))()))", "010100")
print(ans)
