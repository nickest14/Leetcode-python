# 190. Reverse Bits


class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            bit = (n >> i) & 1
            ans += (bit << (31 - i))
        return ans


ans = Solution().reverseBits(int('00000010100101000001111010011100'))
print(ans)
