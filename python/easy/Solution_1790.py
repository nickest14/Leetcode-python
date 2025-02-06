# 1790. Check if One String Swap Can Make Strings Equal


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        diff: list[int] = []
        for i, (c1, c2) in enumerate(zip(s1, s2)):
            if c1 != c2:
                diff.append(i)
                if len(diff) > 2:
                    return False
                    
        return len(diff) == 2 and s1[diff[0]] == s2[diff[1]] and s1[diff[1]] == s2[diff[0]]


ans = Solution().areAlmostEqual("bank", "kanb")
print(ans)
