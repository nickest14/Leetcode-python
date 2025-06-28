# 2311. Longest Binary Subsequence Less Than or Equal to K


class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n: int = len(s)
        zeros: int = s.count("0")
        ones: int = 0
        value: int = 0
        power: int = 1

        for i in range(n - 1, -1, -1):
            if s[i] == "1":
                if value + power > k:
                    continue
                value += power
                ones += 1
            power <<= 1
            if power > k:
                break

        return zeros + ones


ans = Solution().longestSubsequence("1001010", 5)
print(ans)
