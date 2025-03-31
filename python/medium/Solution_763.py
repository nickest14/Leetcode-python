# 763. Partition Labels

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans: list[int] = []
        last_occurence: dict[int, int] = {}
        for ind, c in enumerate(s):
            last_occurence[c] = ind

        goal, cur_len = 0, 0
        for ind, c in enumerate(s):
            goal = max(goal, last_occurence[c])
            cur_len += 1
            if goal == ind:
                ans.append(cur_len)
                cur_len = 0
        return ans


ans = Solution().partitionLabels("ababcbacadefegdehijhklij")
print(ans)
