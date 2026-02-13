# 3713. Longest Balanced Substring I


class Solution:
    def longestBalanced(self, s: str) -> int:
        n: int = len(s)
        ans: int = 0

        for i in range(n):
            freq: list[int] = [0] * 26
            distinct: int = 0
            max_freq: int = 0

            for j in range(i, n):
                idx: int = ord(s[j]) - ord("a")

                if freq[idx] == 0:
                    distinct += 1

                freq[idx] += 1
                max_freq = max(max_freq, freq[idx])

                length: int = j - i + 1

                if length == distinct * max_freq:
                    ans = max(ans, length)

        return ans


ans = Solution().longestBalanced("abbac")
print(ans)
