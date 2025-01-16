# 2429. Minimize XOR


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count_1: int = num1.bit_count()
        count_2: int = num2.bit_count()
        ans: int = num1
        for i in range(32):
            if count_1 > count_2 and num1 & (1 << i):
                ans ^= 1 << i
                count_1 -= 1
            elif count_1 < count_2 and not (num1 & (1 << i)):
                ans ^= 1 << i
                count_1 += 1
            elif count_1 == count_2:
                break

        return ans


ans = Solution().minimizeXor(3, 5)
# ans = Solution().minimizeXor(28, 1)
# ans = Solution().minimizeXor(1, 7)
print(ans)
