# 476. Number Complement

class Solution:
    def findComplement(self, num: int) -> int:
        bit_length = num.bit_length()
        mask = (1 << bit_length) - 1
        return num ^ mask


ans = Solution().findComplement(5)
print(ans)
