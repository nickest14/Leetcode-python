# 567. Permutation in String

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count: dict[str, int] = Counter(s1)
        window_count: dict[str, int] = Counter()
        for ind, c in enumerate(s2):
            window_count[c] += 1
            if ind >= len(s1):
                if window_count[s2[ind - len(s1)]] == 1:
                    del window_count[s2[ind - len(s1)]]
                else:
                    window_count[s2[ind - len(s1)]] -= 1
            if window_count == s1_count:
                return True

        return False

    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     if len(s1) > len(s2):
    #         return False

    #     s1_count, s2_count = [0] * 26, [0] * 26
    #     for i in range(len(s1)):
    #         s1_count[ord(s1[i]) - ord('a')] += 1
    #         s2_count[ord(s2[i]) - ord('a')] += 1

    #     matches = 0
    #     for i in range(26):
    #         matches += 1 if s1_count[i] == s2_count[i] else 0

    #     l = 0
    #     for r in range(len(s1), len(s2)):
    #         if matches == 26:
    #             return True
    #         index = ord(s2[r]) - ord('a')
    #         s2_count[index] += 1
    #         if s1_count[index] == s2_count[index]:
    #             matches += 1
    #         elif s1_count[index] + 1 == s2_count[index]:
    #             matches -= 1

    #         index = ord(s2[l]) - ord('a')
    #         s2_count[index] -= 1
    #         if s1_count[index] == s2_count[index]:
    #             matches += 1
    #         elif s1_count[index] - 1 == s2_count[index]:
    #             matches -= 1
    #         l += 1

    #     return matches == 26


ans = Solution().checkInclusion('ab', 'eidbaooo')
print(ans)
