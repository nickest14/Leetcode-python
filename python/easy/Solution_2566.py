# 2566. Maximum Difference by Remapping a Digit


class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str: str = str(num)

        min_ch: str = next((ch for ch in num_str if ch != "0"), "0")
        min_str: str = num_str.replace(min_ch, "0")

        max_ch: str = next((ch for ch in num_str if ch != "9"), "9")
        max_str: str = num_str.replace(max_ch, "9")

        return int(max_str) - int(min_str)


ans = Solution().minMaxDifference(11891)
print(ans)
