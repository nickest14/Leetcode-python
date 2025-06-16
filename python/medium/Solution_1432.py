# 1432. Max Difference You Can Get From Changing an Integer

class Solution:
    def maxDiff(self, num: int) -> int:
        min_str = max_str = str(num)

        max_ch: str = next((ch for ch in max_str if ch != "9"), "9")
        max_str: str = max_str.replace(max_ch, "9")

        for i, digit in enumerate(min_str):
            if (i == 0 and digit != "1") or (i > 0 and digit != "0" and digit != min_str[0]):
                min_str = min_str.replace(digit, "0" if i > 0 else "1")
                break

        return int(max_str) - int(min_str)


ans = Solution().maxDiff(555)
print(ans)
