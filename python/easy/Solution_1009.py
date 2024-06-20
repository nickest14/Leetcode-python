# 1009. Complement of Base 10 Integer

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        mask = n
        mask |= mask >> 1
        mask |= mask >> 2
        mask |= mask >> 4
        mask |= mask >> 8
        mask |= mask >> 16
        return mask ^ n


ans = Solution().bitwiseComplement(25)
print(ans)
