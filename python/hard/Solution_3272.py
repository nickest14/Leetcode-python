# 3272. Find the Count of Good Integers

from math import factorial
from collections import Counter


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        palindromes: list[int] = []

        half_len: int = (n + 1) // 2
        lower_bound: int = 10 ** (half_len - 1)
        upper_bound: int = 10**half_len

        for half in range(lower_bound, upper_bound):
            half_str = str(half)
            if n % 2 == 0:
                full_str = half_str + half_str[::-1]
            else:
                full_str = half_str + half_str[-2::-1]
            palindromes.append(int(full_str))

        divisible_palindromes = [str(num) for num in palindromes if num % k == 0]

        unique_digit_signatures = set()
        for num_str in divisible_palindromes:
            sorted_digits = "".join(sorted(num_str))
            unique_digit_signatures.add(sorted_digits)

        ans: int = 0

        for digit_str in unique_digit_signatures:
            freq_map = Counter(digit_str)
            total = factorial(len(digit_str))
            for freq in freq_map.values():
                total //= factorial(freq)
            ans += total

            if "0" in freq_map:
                freq_map["0"] -= 1
                zero_start_permutations = factorial(len(digit_str) - 1)
                for freq in freq_map.values():
                    zero_start_permutations //= factorial(freq)
                ans -= zero_start_permutations

        return ans


ans = Solution().countGoodIntegers(3, 5)
print(ans)
