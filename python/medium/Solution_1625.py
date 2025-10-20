# 1625. Lexicographically Smallest String After Applying Operations


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited: set[str] = set([s])
        ans: str = s
        q: list[str] = [s]

        while q:
            cur: str = q.pop(0)
            if cur < ans:
                ans = cur

            chars: list[str] = list(cur)
            for i in range(1, len(chars), 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            added = "".join(chars)
            if added not in visited:
                visited.add(added)
                q.append(added)

            rotated = cur[-b:] + cur[:-b]
            if rotated not in visited:
                visited.add(rotated)
                q.append(rotated)

        return ans


ans = Solution().findLexSmallestString("5525", 9, 2)
print(ans)
