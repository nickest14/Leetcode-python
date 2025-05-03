# 1007. Minimum Domino Rotations For Equal Row


from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(target: int) -> int:
            top_flips: int = 0
            bottom_flips: int = 0
            for t, b in zip(tops, bottoms):
                if t != target and b != target:
                    return -1
                if t != target:
                    top_flips += 1
                elif b != target:
                    bottom_flips += 1
            return min(top_flips, bottom_flips)

        ans: int = check(tops[0])
        if ans != -1 or tops[0] == bottoms[0]:
            return ans
        return check(bottoms[0])


ans = Solution().minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2])
print(ans)
