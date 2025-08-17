# 1323. Maximum 69 Number


class Solution:
    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace("6", "9", 1))


ans = Solution().maximum69Number(9669)
print(ans)
