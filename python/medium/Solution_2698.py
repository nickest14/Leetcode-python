# 2698. Find the Punishment Number of an Integer


class Solution:
    def __init__(self):
        self.memo: dict[tuple[int, int], bool] = {}

    def canPartition(self, num: int, target: int) -> bool:
        key = (num, target)
        if key in self.memo:
            return self.memo[key]

        if target < 0 or num < target:
            return False

        if num == target:
            return True

        s = str(num)
        for i in range(len(s)):
            left = int(s[: i + 1])
            if target - left < 0:
                continue
            right = int(s[i + 1 :] or "0")

            if self.canPartition(right, target - left):
                self.memo[key] = True
                return True

        self.memo[key] = False
        return False

    def punishmentNumber(self, n: int) -> int:
        ans: int = 0
        for num in range(1, n + 1):
            squr: int = num * num
            if self.canPartition(squr, num):
                ans += squr

        return ans


ans = Solution().punishmentNumber(10)
print(ans)
