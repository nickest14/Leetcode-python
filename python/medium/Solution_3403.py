# 3403. Find the Lexicographically Largest String From the Box I

from typing import List


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        ans: str = ""
        m: int = len(word)
        max_part: int = m - numFriends + 1
        for i in range(m):
            tmp: str = ""
            for j in range(i, min(i + max_part, m)):
                tmp += word[j]
            if tmp > ans:
                ans = tmp

        return ans            

ans = Solution().answerString("dbca", 2)

print(ans)
