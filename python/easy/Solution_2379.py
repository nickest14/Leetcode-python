# 2379. Minimum Recolors to Get K Consecutive Black Blocks


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        black_count: int = 0
        ans: int = float('inf')
        for i in range(len(blocks)):
            if i - k >= 0 and blocks[i - k] == 'B':
                black_count -= 1
            if blocks[i] == 'B':
                black_count += 1
            ans = min(ans, k - black_count)

        return ans


ans = Solution().minimumRecolors("WBBWWBBWBW", 7)
print(ans)
