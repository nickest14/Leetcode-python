# 2002. Maximum Product of the Length of Two Palindromic Subsequences

class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        pali = {}  # bitmask: length

        for mask in range(1, 1 << n):  # 1 << n == 2 ** n
            subseq = ""
            for i in range(n):
                if mask & (1 << i):
                    subseq += s[i]
            if subseq == subseq[::-1]:
                pali[mask] = len(subseq)

        ans = 0
        for m1 in pali:
            for m2 in pali:
                if m1 & m2 == 0:  # disjoint
                    ans = max(ans, pali[m1] * pali[m2])

        return ans


ans = Solution().maxProduct("leetcodecom")
print(ans)
