# 1061. Lexicographically Smallest Equivalent String


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent: list[int] = list(range(26))

        def find(x: int) -> int:
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        for i in range(len(s1)):
            char_s1, char_s2 = ord(s1[i]) - ord("a"), ord(s2[i]) - ord("a")
            parent1, parent2 = find(char_s1), find(char_s2)
            if parent1 < parent2:
                parent[parent2] = parent1
            else:
                parent[parent1] = parent2

        ans: str = ""
        for i in baseStr:
            index: int = ord(i) - ord("a")
            ans += chr(find(index) + ord("a"))
        return ans


ans = Solution().smallestEquivalentString("parker", "morris", "parser")
print(ans)
