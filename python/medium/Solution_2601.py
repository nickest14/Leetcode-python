# 2601. Prime Subtraction Operation

from bisect import bisect_left
from typing import List


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def process_prime(max_num: int):
            is_prime: list[bool] = [True] * (max_num + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(max_num ** 0.5 + 1)):
                if is_prime[i]:
                    for j in range(i * i, max_num + 1, i):
                        is_prime[j] = False
            return [i for i in range(2, max_num + 1) if is_prime[i]]

        primes: list[int] = process_prime(1000)

        prev: int = 0
        for i in range(len(nums)):
            pos = bisect_left(primes, nums[i])
            success: bool = False
            for j in range(pos - 1, -1, -1):
                prime = primes[j]
                if nums[i] - prime > prev:
                    nums[i] -= prime
                    success = True
                    break
            if not success and nums[i] <= prev:
                return False

            prev = nums[i]

        return True


ans = Solution().primeSubOperation([4, 9, 6, 10])
print(ans)
