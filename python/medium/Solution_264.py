# 264. Ugly Number II


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        primes: list[int] = [2, 3, 5]
        next_ugly: list[int] = [2, 3, 5]
        increase: list[int] = [1, 1, 1]
        ans: list[int] = [1]

        for _ in range(1, n):
            smallest = min(next_ugly)
            ans.append(smallest)
            for i in range(3):
                if next_ugly[i] == smallest:
                    next_ugly[i] = primes[i] * ans[increase[i]]
                    increase[i] += 1

        return ans[-1]


ans = Solution().nthUglyNumber(15)
print(ans)
