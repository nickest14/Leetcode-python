# 2048. Next Greater Numerically Balanced Number


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def check(x: int) -> bool:
            s = str(x)
            vec = [0] * 10
            for ch in s:
                vec[ord(ch) - 48] += 1
            for ch in s:
                c = ord(ch) - 48
                if c == 0 or vec[c] != c:
                    return False
            return True

        i = n + 1
        while True:
            if check(i):
                return i
            i += 1


ans = Solution().nextBeautifulNumber(1000)
print(ans)
