# 564. Find the Closest Palindrome


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        results: list[str] = []
        length: int = len(n)
        if length == 1:
            return str(int(n) - 1)

        results.append(10 ** length + 1)
        results.append(10 ** (length - 1) - 1)

        mid: int = (length + 1) // 2
        prefix: int = int(n[:mid])
        prefixs: list[int] = [prefix, prefix - 1, prefix + 1]

        for i in prefixs:
            res = str(i)
            if length & 1:
                res = res[:-1]
            peep = str(i) + res[::-1]
            results.append(int(peep))

        min_diff = float('inf')
        ans = tip = int(n)

        for i in range(5):
            if results[i] != tip and min_diff > abs(results[i] - tip):
                min_diff = abs(results[i] - tip)
                ans = results[i]
            elif abs(results[i] - tip) == min_diff:
                ans = min(ans, results[i])

        return str(ans)


ans = Solution().nearestPalindromic("1234")
print(ans)
