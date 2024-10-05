# 2491. Divide Players Into Teams of Equal Skill

from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        team_skill: int = skill[0] + skill[-1]
        ans: int = 0
        for i in range(len(skill) // 2):
            if skill[i] + skill[-i - 1] != team_skill:
                return -1
            ans += skill[i] * skill[-i - 1]

        return ans


ans = Solution().dividePlayers([3, 2, 5, 1, 3, 4])
print(ans)
