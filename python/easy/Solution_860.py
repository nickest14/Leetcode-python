# 860. Lemonade Change

from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_five: int = 0
        count_ten: int = 0

        for bill in bills:
            match bill:
                case 5:
                    count_five += 1
                case 10:
                    if count_five == 0:
                        return False
                    count_ten += 1
                    count_five -= 1
                case _:
                    if count_five >= 1 and count_ten >= 1:
                        count_ten -= 1
                        count_five -= 1
                    elif count_five >= 3:
                        count_five -= 3
                    else:
                        return False

        return True


ans = Solution().lemonadeChange([5, 5, 5, 10, 20])
print(ans)
