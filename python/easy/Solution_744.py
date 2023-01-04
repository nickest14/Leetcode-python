# 744. Find Smallest Letter Greater Than Target

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters)
        while left < right:
            mid = left + (right - left) // 2
            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1
        return letters[0] if left == len(letters) else letters[left]


ans = Solution().nextGreatestLetter(['c', 'f', 'j'], 'g')
print(ans)
