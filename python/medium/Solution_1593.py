# 1593. Split a String Into the Max Number of Unique Substrings


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def fn(i: int, seen: set = set()):
            ans: int = 0
            if i < len(s):
                for j in range(i + 1, len(s) + 1):
                    if s[i: j] not in seen:
                        seen.add(s[i:j])
                        ans = max(ans, 1 + fn(j, seen))
                        seen.remove(s[i:j])
            return ans

        return fn(0)


# ans = Solution().maxUniqueSplit('ababccc')
ans = Solution().maxUniqueSplit('a')
print(ans)
