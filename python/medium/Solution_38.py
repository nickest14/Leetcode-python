# 38. Count and Say


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        cur: str = "1"
        for _ in range(2, n + 1):
            next: str = ""
            count: int = 1
            for j in range(len(cur)):
                if j < len(cur) - 1 and cur[j] == cur[j + 1]:
                    count += 1
                else:
                    next += str(count) + cur[j]
                    count = 1
            cur = next
        return cur


ans = Solution().countAndSay(5)
print(ans)
