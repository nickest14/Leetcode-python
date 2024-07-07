# 2582. Pass the Pillow

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        round_count = (n - 1) * 2
        pass_count = time % round_count
        if pass_count >= n:
            return n - (pass_count - n) - 1
        else:
            return 1 + pass_count


ans = Solution().passThePillow(4, 5)
print(ans)
