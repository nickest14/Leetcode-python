# 1945. Sum of Digits of String After Convert


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        number = ''.join(str(ord(c) - ord('a') + 1) for c in s)

        for _ in range(k):
            number = str(sum(int(c) for c in number))

        return int(number)


ans = Solution().getLucky('leetcode', 2)
print(ans)
