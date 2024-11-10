# 3133. Minimum Array End


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1  # x is the start of array nums, so minus n by 1
        binary_x = list(bin(x)[2:])
        binary_n = list(bin(n)[2:])
        cur_n = len(binary_n) - 1
        for i in range(len(binary_x) - 1, -1, -1):
            if binary_x[i] == "1":
                continue
            binary_x[i] = binary_n[cur_n]
            cur_n -= 1
            if cur_n == -1:
                break
        if cur_n >= 0:
            binary_x = binary_n[0:cur_n + 1] + binary_x

        return int("".join(binary_x), 2)


# class Solution:
#     def minEnd(self, n: int, x: int) -> int:
#         nums: list[int] = [x]
#         current = x

#         for _ in range(1, n):
#             next_val = current + 1
#             while (next_val & x) != x:
#                 next_val += 1
#             nums.append(next_val)
#             current = next_val

#         return nums[-1]


ans = Solution().minEnd(8, 4)
# ans = Solution().minEnd(2, 7)
print(ans)
