# 17. Letter Combinations of a Phone Number

from typing import List
import collections


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return ''
        mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        result = collections.deque([''])
        for d in digits:
            for _ in range(len(result)):
                prev = result.popleft()
                for letter in mapping[int(d)]:
                    result.append(prev + letter)
        return result


ans = Solution().letterCombinations('234')
print(ans)
