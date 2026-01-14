# 3453. Separate Squares I

from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def area_below(y: float) -> float:
            area: float = 0.0
            for _, y0, side_len in squares:
                if y0 < y:
                    h = min(y - y0, side_len)
                    area += h * side_len
            return area
        
        total_area: float = sum(side_len * side_len for _, _, side_len in squares)
        target_area = total_area / 2
        
        low, high = 0.0, max(y + side_len for _, y, side_len in squares)
        
        while high - low > 1e-5:
            mid: float = (low + high) / 2.0
            if area_below(mid) < target_area:
                low = mid
            else:
                high = mid
        
        return high


ans = Solution().separateSquares([[0, 0, 1], [2, 2, 1]])
print(ans)
