# 2410. Maximum Matching of Players With Trainers

from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        count: int = 0
        i = j = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1

        return count


ans = Solution().matchPlayersAndTrainers([4, 7, 9], [8, 2, 5, 8])
print(ans)
