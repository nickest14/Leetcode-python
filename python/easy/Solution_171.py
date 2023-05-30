# 171. Excel Sheet Column Number


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        length = len(columnTitle)
        return sum((ord(c) - ord('A') + 1) * 26 ** (length - i - 1) for i, c in enumerate(columnTitle))


ans = Solution().titleToNumber('AAA')
print(ans)
