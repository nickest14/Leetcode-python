# 1143. Longest Common Subsequence


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]

    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     matrix = [[0 for _ in range(len(text2))] for _ in range(len(text1))]
    #     for i in range(len(text1)):
    #         for j in range(len(text2)):
    #             if text1[i] == text2[j]:
    #                 matrix[i][j] = 1 + (matrix[i - 1][j - 1] if i >= 1 and j >= 1 else 0)
    #             else:
    #                 left = matrix[i - 1][j] if i >= 1 else 0
    #                 right = matrix[i][j - 1] if j >= 1 else 0
    #                 matrix[i][j] = max(left, right)
    #     return matrix[len(text1) - 1][len(text2) - 1]


ans = Solution().longestCommonSubsequence('abcde', 'ace')
# ans = Solution().longestCommonSubsequence('oxcpqrsvwf', 'shmtulqrypy')
print(ans)
