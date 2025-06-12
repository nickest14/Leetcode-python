# 3445. Maximum Difference Between Even and Odd Frequency II

from typing import List


class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n: int = len(s)
        freq: List[List[int]] = [[0] * (n + 1) for _ in range(5)]
        for i in range(n):
            for d in range(5):
                freq[d][i + 1] = freq[d][i]
            freq[int(s[i])][i + 1] += 1

        ans: int = float("-inf")
        for a in range(5):
            if freq[a][n] == 0:
                continue
            for b in range(5):
                if a == b or freq[b][n] == 0:
                    continue
                ans = max(ans, self.maxDfromAtoB(a, b, k, n, freq))
        return ans

    def maxDfromAtoB(
        self, a: int, b: int, k: int, n: int, freq: List[List[int]]
    ) -> int:
        cnt: int = float("-inf")
        mod: int = 10**8
        min_freq: List[List[int]] = [[mod, mod], [mod, mod]]
        freq_a: int = 0
        freq_b: int = 0
        prev_a: int = 0
        prev_b: int = 0
        left: int = 0
        for right in range(k - 1, n):
            freq_a = freq[a][right + 1]
            freq_b = freq[b][right + 1]
            while right - left + 1 >= k and freq_b - prev_b >= 2:
                min_freq[prev_a & 1][prev_b & 1] = min(
                    min_freq[prev_a & 1][prev_b & 1], prev_a - prev_b
                )
                prev_a = freq[a][left + 1]
                prev_b = freq[b][left + 1]
                left += 1
            cnt = max(cnt, freq_a - freq_b - min_freq[1 - (freq_a & 1)][freq_b & 1])
        return cnt


ans = Solution().maxDifference("12233", 4)
print(ans)
