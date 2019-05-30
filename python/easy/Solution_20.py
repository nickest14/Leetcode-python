class Solution:
    pair = {
        '[': ']',
        '{': '}',
        '(': ')'
    }

    def isValid(self, s: str) -> bool:
        if s:
            li = []
            for i in s:
                if i in self.pair.keys():
                    li.append(i)
                else:
                    if len(li) == 0:
                        return False
                    inside = li.pop()
                    if not self.pair[inside] == i:
                        return False
            if len(li) != 0:
                return False
        return True


ans = Solution().isValid('{[]}')
print(ans)
