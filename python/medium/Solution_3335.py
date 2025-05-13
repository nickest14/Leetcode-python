# 3335. Total Characters in String After Transformations I


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod: int = 10**9 + 7
        cnt: list[int] = [0] * 26
        z: int = 25
        ans: int = len(s)

        for c in s:
            cnt[ord(c) - ord("a")] += 1

        for _ in range(t):
            ans = (ans + cnt[z]) % mod
            cnt[(z + 1) % 26] = (cnt[(z + 1) % 26] + cnt[z]) % mod
            z = (z + 25) % 26

        return ans


ans = Solution().lengthAfterTransformations("abcyy", 2)
print(ans)
