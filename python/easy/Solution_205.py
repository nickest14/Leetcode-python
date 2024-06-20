# 205. Isomorphic Strings


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


ans = Solution().isIsomorphic('qqw', 'kkz')
print(ans)
