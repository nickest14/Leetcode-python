# 2264. Largest 3-Same-Digit Number in String


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans: str = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                ans = max(ans, num[i : i + 3])
        return ans


ans = Solution().largestGoodInteger("6777133339")
print(ans)
