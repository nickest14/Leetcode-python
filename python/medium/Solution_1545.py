# 1545. Find Kth Bit in Nth Binary String


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rev_inv(s: str):
            s = ''.join('1' if c == '0' else '0' for c in s)
            return s[::-1]

        s: str = '0'
        while n > 1:
            s = s + '1' + rev_inv(s)
            n -= 1
        return s[k - 1]


# ans = Solution().findKthBit(3, 1)
ans = Solution().findKthBit(4, 11)
print(ans)
