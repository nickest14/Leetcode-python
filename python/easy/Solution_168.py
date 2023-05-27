# 168. Excel Sheet Column Title


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber > 0:
            columnNumber, r = divmod(columnNumber - 1, 26)
            ans.append(chr(ord('A') + r))
        return ''.join(ans[::-1])


ans = Solution().convertToTitle(701)
print(ans)
