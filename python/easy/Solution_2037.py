# 2037. Minimum Number of Moves to Seat Everyone

from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        return sum(abs(seat - student) for seat, student in zip(seats, students))


seats = [3, 1, 5]
students = [2, 7, 4]
ans = Solution().minMovesToSeat(seats, students)
print(ans)
