# 438. Find All Anagrams in a String

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start_ind = 0
        s_map, p_map = {}, {}
        ans = []
        for char in p:
            p_map[char] = p_map.get(char, 0) + 1
        for i in range(len(s)):
            s_map[s[i]] = s_map.get(s[i], 0) + 1

            if i >= len(p) - 1:
                if s_map == p_map:
                    ans.append(start_ind)

                s_map[s[start_ind]] -= 1
                if s_map[s[start_ind]] == 0:
                    del s_map[s[start_ind]]
                start_ind += 1

        return ans


ans = Solution().findAnagrams("cbaebabacd", "abc")
print(ans)
