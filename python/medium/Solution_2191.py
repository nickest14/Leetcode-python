# 2191. Sort the Jumbled Numbers

from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def translate_to_int(num: int) -> int:
            s: str = ''
            for _, val in enumerate(str(num)):
                s += str(mapping[int(val)])
            return int(s)

        number_mapping: dict[int, int] = {}
        for num in nums:
            number_mapping[num] = translate_to_int(num)

        nums.sort(key=lambda val: number_mapping[val])
        return nums


ans = Solution().sortJumbled([8, 9, 4, 0, 2, 1, 3, 5, 7, 6], [991, 338, 38])
print(ans)
