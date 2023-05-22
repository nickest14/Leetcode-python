# 8. String to Integer (atoi)


class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.lstrip()
        sign = 1
        if s and s[0] in '+-':
            if s[0] == '-':
                sign = -1
            s = s[1:]
        num = 0
        for c in s:
            if not c.isdigit():
                break
            num = 10 * num + int(c)
        return max(-2**31, min(2**31 - 1, sign * num))


ans = Solution().myAtoi('  -99ABC')
print(ans)
