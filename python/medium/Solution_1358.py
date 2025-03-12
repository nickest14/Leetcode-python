# 1358. Number of Substrings Containing All Three Characters


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans: int = 0
        left: int = 0
        freq: dict[str, int] = {"a": 0, "b": 0, "c": 0}
        for right in range(len(s)):
            freq[s[right]] += 1
            while freq["a"] > 0 and freq["b"] > 0 and freq["c"] > 0:
                freq[s[left]] -= 1
                left += 1
            ans += left
        return ans


ans = Solution().numberOfSubstrings("abcabc")
# ans = Solution().numberOfSubstrings("abcaaa")
print(ans)
