# 2977. Minimum Cost to Convert String II

from typing import List


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        words: set[str] = set(original) | set(changed)
        word_to_id: dict[str, int] = {word: i for i, word in enumerate(words)}
        num_words: int = len(words)

        dist = [[float("inf")] * num_words for _ in range(num_words)]
        for i in range(num_words):
            dist[i][i] = 0

        for u_str, v_str, c in zip(original, changed, cost):
            u, v = word_to_id[u_str], word_to_id[v_str]
            dist[u][v] = min(dist[u][v], c)

        for k in range(num_words):
            for i in range(num_words):
                if dist[i][k] == float("inf"):
                    continue
                for j in range(num_words):
                    if dist[k][j] == float("inf"):
                        continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        lengths = sorted(list(set(len(w) for w in words)))

        n: int = len(source)
        dp: list[int] = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            if source[i - 1] == target[i - 1]:
                dp[i] = min(dp[i], dp[i - 1])

            for length in lengths:
                if length > i:
                    break
                j = i - length
                sub_s = source[j:i]
                sub_t = target[j:i]

                if sub_s in word_to_id and sub_t in word_to_id:
                    u, v = word_to_id[sub_s], word_to_id[sub_t]
                    if dist[u][v] != float("inf"):
                        dp[i] = min(dp[i], dp[j] + dist[u][v])

        return int(dp[n]) if dp[n] != float("inf") else -1


source = "abcd"
target = "acbe"
original = ["a", "b", "c", "c", "e", "d"]
changed = ["b", "c", "b", "e", "b", "e"]
cost = [2, 5, 5, 1, 2, 20]
ans = Solution().minimumCost(source, target, original, changed, cost)
print(ans)
