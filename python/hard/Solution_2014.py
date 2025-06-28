# 2014. Longest Subsequence Repeated k Times

from collections import deque


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def is_k(sub: str, t: str, k: int) -> bool:
            count = i = 0
            for ch in t:
                if i < len(sub) and ch == sub[i]:
                    i += 1
                    if i == len(sub):
                        i = 0
                        count += 1
                        if count == k:
                            return True
            return False

        ans: str = ""
        q: deque[str] = deque([""])
        while q:
            curr: str = q.popleft()
            for ch in map(chr, range(ord("a"), ord("z") + 1)):
                next: str = curr + ch
                if is_k(next, s, k):
                    ans = next
                    q.append(next)

        return ans


ans = Solution().longestSubsequenceRepeatedK("letsleetcode", 2)
print(ans)
