# 657. Robot Return to Origin


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for move in moves:
            if move in 'UD':
                y += 1 if move == 'U' else -1
            else:
                x += 1 if move == 'R' else -1
        return (x, y) == (0, 0)


ans = Solution().judgeCircle('UDRL')
print(ans)
