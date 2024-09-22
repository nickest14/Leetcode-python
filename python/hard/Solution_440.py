# 440. K-th Smallest in Lexicographical Order


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_prefix(p, n):
            count: int = 0
            cur = p
            next_p = p + 1
            while cur <= n:
                count += min(next_p, n + 1) - cur
                cur *= 10
                next_p *= 10
            return count

        cur: int = 1
        k -= 1
        while k > 0:
            count = count_prefix(cur, n)
            if k >= count:
                k -= count
                cur += 1
            else:
                cur *= 10
                k -= 1

        return cur

    # # Time Limit Exceeded
    # def findKthNumber(self, n: int, k: int) -> int:
    #     ans: int = -1
    #     cur: int = 1
    #     for _ in range(k):
    #         ans = cur
    #         if cur * 10 <= n:
    #             cur *= 10
    #         else:
    #             if cur >= n:
    #                 cur //= 10
    #             cur += 1
    #             while cur % 10 == 0:
    #                 cur //= 10

    #     return ans


# ans = Solution().findKthNumber(19, 10)
ans = Solution().findKthNumber(50, 14)
print(ans)
