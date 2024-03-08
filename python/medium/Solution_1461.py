# 1461. Check If a String Contains All Binary Codes of Size K


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len(set(s[i: i + k] for i in range(len(s) - k + 1))) == 2 ** k


ans = Solution().hasAllCodes("00110110", 2)
print(ans)
