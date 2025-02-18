# 1079. Letter Tile Possibilities


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        char_count: list[int] = [0] * 26
        for c in tiles:
            char_count[ord(c) - ord("A")] += 1

        def build_char():
            total_count: int = 0
            for i in range(26):
                if char_count[i]:
                    total_count += 1
                    char_count[i] -= 1
                    total_count += build_char()
                    char_count[i] += 1
            return total_count

        return build_char()


ans = Solution().numTilePossibilities("ABC")
# ans = Solution().numTilePossibilities("AAABBC")
print(ans)
