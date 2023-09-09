# 134. Gas Station

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas, remaining_gas = 0, 0
        start_index = 0

        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            remaining_gas += gas[i] - cost[i]
            if remaining_gas < 0:
                remaining_gas = 0
                start_index = i + 1

        if total_gas >= 0:
            return start_index
        else:
            return -1


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
ans = Solution().canCompleteCircuit(gas, cost)
print(ans)
