# 1456. Maximum Number of Vowels in a Substring of Given Length


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, ans, total = 0, 0, 0
        vowels = 'aeiou'
        for r in range(len(s)):
            if s[r] in vowels:
                total += 1
            if (r - l + 1) > k:
                if s[l] in vowels:
                    total -= 1
                l += 1
            ans = max(ans, total)

        return ans


ans = Solution().maxVowels('leetcode', 3)
print(ans)


# lookup = {sum(d > distanceThreshold for d in row): i for i, row in enumerate(matrix)}

# lookup = {}
# for i, row in enumerate(matrix):
#     count = 0
#     for d in row:
#         if d > distanceThreshold:
#             count += 1
#     lookup[count] = i
