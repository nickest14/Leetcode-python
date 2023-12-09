# 763. Partition Labels

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        count = {}
        for ind, c in enumerate(s):
            count[c] = ind

        goal, cur_len = 0, 0
        for ind, c in enumerate(s):
            goal = max(goal, count[c])
            cur_len += 1
            if goal == ind:
                ans.append(cur_len)
                cur_len = 0
        return ans


ans = Solution().partitionLabels('ababcbacadefegdehijhklij')
print(ans)
