# 2843. Count Symmetric Integers


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans: int = 0

        for num in range(low, high + 1):
            s = str(num)
            if len(s) % 2 == 0:
                mid = len(s) // 2
                if sum(map(int, s[:mid])) == sum(map(int, s[mid:])):
                    ans += 1
        return ans


ans = Solution().countSymmetricIntegers(1, 100)
print(ans)
