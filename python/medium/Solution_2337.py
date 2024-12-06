# 2337. Move Pieces to Obtain a String


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start == target:
            return True
        pending_l: int = 0
        waiting_r: int = 0

        for cur, goal in zip(start, target):
            if cur == 'R':
                if pending_l > 0:
                    return False
                waiting_r += 1
            if goal == 'L':
                if waiting_r > 0:
                    return False
                pending_l += 1
            if goal == 'R':
                if waiting_r == 0:
                    return False
                waiting_r -= 1
            if cur == 'L':
                if pending_l == 0:
                    return False
                pending_l -= 1

        return pending_l == 0 and waiting_r == 0


# ans = Solution().canChange('_L__R__R_', 'L______RR')
# ans = Solution().canChange('RR__', '__RR')
ans = Solution().canChange('R_L_', '__LR')
print(ans)
