# 1784. Check if Binary String Has at Most One Segment of Ones


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        zero: bool = False
        for c in s:
            if c == "0":
                zero = True
            elif zero:
                return False

        return True


ans = Solution().checkOnesSegment("1001")
print(ans)
